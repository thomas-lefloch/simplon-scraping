import scrapy
from scrapy.item import Item, Field


class ItemCategories(scrapy.Item):
    id = Field()
    name = Field()
    page_list = Field()
