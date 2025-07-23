import scrapy
from scrapy.item import Item, Field


class ItemProducts(scrapy.Item):
    id = Field(required=True)  # sku
    name = Field(required=True)
    base_price = Field()  # Prix du produit hors promo (en euro)
    price = Field(required=True)  # Prix actuel du produit (en euro)
    vat_included = Field(required=True)  # Booléen qui indique si la TVA est incluse
    unit = Field()  # Unite (m2 / kg / unité / ml)
    url = Field(required=True)
    category_id = Field()
    image = Field()
