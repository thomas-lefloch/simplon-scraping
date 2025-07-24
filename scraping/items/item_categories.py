import scrapy
from scrapy.item import Item, Field


class ItemCategories(scrapy.Item):
    id = Field(required=True)
    name = Field(required=True)
    page_list = Field()
