import scrapy


class BoutiqueParquetSpider(scrapy.Spider):
    name = "boutique-parquet"
    allowed_domains = ["boutique-parquet.com"]
    start_urls = ["https://boutique-parquet.com"]

    def parse(self, response):
        pass
