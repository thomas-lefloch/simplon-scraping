from itemadapter import ItemAdapter
import scrapy

class FilterCategoryPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        category_id = adapter.get("id", "")
        # D'apres notre analyse sur le site, on a remarqué que les produits présent sur les marques apparaissent deja dans d'autres catégories
        if category_id.startswith("/marque"):
            raise scrapy.exceptions.DropItem(f"Catégorie exclue : {category_id}")
        
        return item
