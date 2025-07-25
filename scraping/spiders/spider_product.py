import scrapy
from urllib.parse import urlparse
import json 

from scraping.items.item_products import ItemProducts


def clean_price(raw):
    """
    Nettoie le prix  en supprimant le symbole euro et en remplaçant la virgule par un point.
    Si la valeur est vide ou None, retourne None.
    """
    if raw:
        return raw.replace("€", "").replace(",", ".")
    return None
    
def clean_unit(raw):
    """
    Nettoie l'unité extraite en supprimant les espaces inutiles.
    Si la valeur est 'TTC', elle est remplacée par 'unité'.
    Sinon, renvoie le dernier mot de la chaîne (m^2, kg, ml).
    """    
    if not raw:
        return None
    raw = raw.strip()
    # Juste "TTC"
    if raw.upper() == "TTC":
        return "unité"
    return  raw.split()[-1]
    
class ProductSpider(scrapy.Spider):
    name = "products"
    allowed_domains = ["boutique-parquet.com"]

    def __init__(self, urls=None, *args, **kwargs):
        if not urls:
            raise AttributeError("Url missing")
        self.start_urls = urls
        super(ProductSpider, self).__init__(*args, **kwargs)

    def parse_products(self, response):
        
        sku_map = {}  # Dictionnaire pour récupérer les URL à leur SKU

        # On récupère le script JSON dans la page
        scripts = response.css('script[type="application/ld+json"]::text').getall()
        for script in scripts:
            try:
                # Charger le contenu JSON
                data = json.loads(script)
            
                # Vérifie que c'est un objet ItemList (qui contient tous les produits visibles sur la page)
                if isinstance(data, dict) and data.get("@type") == "ItemList":
                    for product in data.get("itemListElement", []):
                        item = product.get("item", {})

                        # Récupérer le SKU et l'URL du produit
                        sku = item.get("sku")
                        url = item.get("url")

                        if sku and url:
                            # Nettoyage des URL pour éviter les erreurs de correspondance
                            sku_map[url.strip()] = sku.strip()
                
            except Exception as e:
                self.logger.warning(f"Erreur parsing JSON: {e}")
        
                            
                   
                            
        products = response.css("ol.products.list.items.product-items li.product-item")
        for product in products:
            name = product.css("a.product-item-link::text").get()
            base_price = clean_price(product.css(".old-price .price::text").get())
            price = clean_price(product.css("span.price::text").get())
            raw_unit = product.css("div.price-box span.lbpunit::text").get()
            unit = clean_unit(raw_unit)
            vat_included = True if raw_unit and raw_unit.strip().upper().startswith("TTC") else False           
            url = product.css("a.product-item-link::attr(href)").get().strip()
            id = sku_map.get(url.strip(), "")
            image = product.css("img.product-image-photo::attr(src)").get()
            category_id = urlparse(response.request.url).path

            yield ItemProducts(
                    {
                        "id": id,
                        "name": name,
                        "base_price": base_price,
                        "price": price,
                        "unit": unit,
                        "vat_included" : vat_included,
                        "url": url,
                        "image": image,
                        "unit" : unit,
                        "category_id": category_id,
                    }
                )
            # gestion de la pagination 
            next_page = response.css("a.action.next::attr(href)").get()
            if next_page:
                yield response.follow(next_page, callback=self.parse)

    def parse(self, response):
        yield from self.parse_products(response)
