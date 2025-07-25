import scrapy
from scrapy.item import Item, Field


class ItemProducts(scrapy.Item):
    """
    Représente un produit extrait du site boutique-parquet.com.

    Attributes:
        id (str) : Identifiant unique du produit qui est le SKU (obligatoire).
        name (str) : Nom du produit (obligatoire).
        base_price (float) : Prix initial (hors promotion), en euros.
        price (float) : Prix actuel du produit (avec ou sans promotion), en euros (obligatoire).
        vat_included (bool) : Indique si le prix inclut la TVA — (obligatoire).
        unit (str) : Unité de mesure (ex : m², kg, unité, ml).
        url (str) : URL de la page du produit (obligatoire).
        category_id (str) : Identifiant de la catégorie associée.
        image (str) : URL de l'image du produit.
    """
    id = Field(required=True)  
    name = Field(required=True)
    base_price = Field(value_type=float)  
    price = Field(required=True, value_type=float)  
    vat_included = Field(required=True, value_type=bool)  
    unit = Field()  
    url = Field(required=True)
    category_id = Field()
    image = Field()
