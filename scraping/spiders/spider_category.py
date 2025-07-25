import scrapy
from urllib.parse import urlparse

from scraping.items.item_categories import ItemCategories


class CategorySpider(scrapy.Spider):
    """
    Spider qui extrait les catégories de produits depuis boutique-parquet.com.
    """
    name = "categories"
    allowed_domains = ["boutique-parquet.com"]
    start_urls = ["https://boutique-parquet.com"]

    menu_id = "#header-menu-all-product"

    def extract_id_from_url(self, url):
        """
        Args:
            url (str): Un string parsable par urlib.parse
        Returns: 
            str: La chemin de l'url
        """
        return urlparse(url).path

    def filter_category(self, category_id):
        """
        Filtre les catégories de marques car les produits apparaissent deja dans d'autres catégories.
        """
        if category_id.startswith("/marque"):
            self.logger.info(f"Catégorie exclue : {category_id}")
            return ""
        return category_id

    def parse_upper_categories(self, response):
        """ 
        Extrait les catégories de niveau 0 (principales) depuis le menu.
        """        
        upper_categories = response.css(f"{self.menu_id} li.level0 > a")
        for category in upper_categories:
            yield ItemCategories(
                {
                    "id": self.filter_category(
                        self.extract_id_from_url(category.attrib["href"])
                    ),
                    "name": category.css("span::text").get(),
                    "page_list": "",
                }
            )

    def parse_sub_categories(self, response):
        """
        Extrait les sous catégories de niveau 1 depuis le menu.
        """        
        sub_categories = response.css(f"{self.menu_id} li.level1 > a")
        for category in sub_categories:
            yield ItemCategories(
                {
                    "id": self.filter_category(
                        self.extract_id_from_url(category.attrib["href"])
                    ),
                    "name": category.css("span::text").get(),
                    "page_list": category.attrib["href"],
                }
            )

    def parse(self, response):
        yield from self.parse_upper_categories(response)
        yield from self.parse_sub_categories(response)
