import scrapy
from scrapy.item import Item, Field


class ItemProducts(scrapy.Item):
    id = Field()  # sku
    name = Field()
    base_price = Field()  # Prix du produit hors promo (en euro)
    price = Field()  # Prix actuel du produit (en euro)
    unit = Field()  # Unite (m2 / kg / unité)
    url = Field()
    category_id = Field()
    image = Field()
