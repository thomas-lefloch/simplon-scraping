import scrapy
from scrapy.item import Item, Field


class ItemProducts(scrapy.Item):
    id = Field(required=True)  # sku
    name = Field(required=True)
    base_price = Field(value_type=float)  # Prix du produit hors promo (en euro)
    price = Field(required=True, value_type=float)  # Prix actuel du produit (en euro)
    vat_included = Field(
        required=True, value_type=bool
    )  # Booléen qui indique si la TVA est incluse
    unit = Field()  # Unite (m2 / kg / unité / ml)
    url = Field(required=True)
    category_id = Field()
    image = Field()
