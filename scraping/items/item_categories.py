import scrapy
from scrapy.item import Item, Field


class ItemCategories(scrapy.Item):
    """
    Représente une catégorie de produit.

    Attributes:
        id (str) : Identifiant unique de la catégorie (obligatoire).
        name (str) : Nom de la catégorie (obligatoire).
        page_list (str) : URL de la page listant les produits de cette catégorie.
    """
    id = Field(required=True)
    name = Field(required=True)
    page_list = Field()
    