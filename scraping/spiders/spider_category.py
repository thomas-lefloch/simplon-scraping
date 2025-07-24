import scrapy
from urllib.parse import urlparse

from scraping.items.item_categories import ItemCategories

class CategorySpider(scrapy.Spider):
    name = "categories"
    allowed_domains = ["boutique-parquet.com"]
    start_urls = ["https://boutique-parquet.com"]

    menu_id = "#header-menu-all-product"

    def extract_id_from_url(self, url):
        return urlparse(url).path
    
    def filter_category(self, category_id) : 
        # D'apres notre analyse sur le site, on a remarqué que les produits présent sur les marques apparaissent deja dans d'autres catégories
        if category_id.startswith("/marque"):
            self.logger.info(f"Catégorie exclue : {category_id}")
            return None
        return category_id

    def parse_upper_categories(self, response):
        upper_categories = response.css(f"{self.menu_id} li.level0 > a")
        for category in upper_categories:
            yield ItemCategories(
                {
                    "id": self.filter_category(self.extract_id_from_url(category.attrib["href"])),
                    "name": category.css("span::text").get(),
                    "page_list": "",
                }
            )

    def parse_sub_categories(self, response):
        sub_categories = response.css(f"{self.menu_id} li.level1 > a")
        for category in sub_categories:
            yield ItemCategories(
                {
                    "id": self.filter_category(self.extract_id_from_url(category.attrib["href"])),
                    "name": category.css("span::text").get(),
                    "page_list": category.attrib["href"],
                }
            )

    def parse(self, response):
        yield from self.parse_upper_categories(response)
        yield from self.parse_sub_categories(response)
        yield ItemCategories({"id": "test","name": "", "page_list": ""})
        yield ItemCategories({"name": "testID", "page_list": ""})

