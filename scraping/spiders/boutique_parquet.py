import scrapy


class BoutiqueParquetSpider(scrapy.Spider):
    name = "boutique-parquet"
    allowed_domains = ["boutique-parquet.com"]
    start_urls = ["https://boutique-parquet.com"]

    menu_id = "#header-menu-all-product"

    def parse_sub_categories(self, response):
        sub_categories = response.css(f'{self.menu_id} li.level1 > a')
        for category in sub_categories:
            yield {
                'name': category.css('span::text').get(),
                'page_list': category.attrib['href']
            }
    
    def parse_upper_categories(self, response):
        upper_categories = response.css(f'{self.menu_id} li.level0 > a')
        for category in upper_categories:
            yield {
                'name': category.css('span::text').get()
            }

    def parse(self, response): 
        yield from self.parse_upper_categories(response)
        yield from self.parse_sub_categories(response)
    


        
