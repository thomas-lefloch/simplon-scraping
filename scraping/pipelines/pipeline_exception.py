from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class MissingIDPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        if "id" not in adapter or not adapter["id"]:
            spider.logger.warning(f"[Info] Champ 'id' manquant ou vide : {adapter}")
            raise DropItem("Missing id")
        
        return item


class MissingNamePipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        if "name" not in adapter or not adapter["name"]:
            spider.logger.warning(f"[Info] Champ 'name' manquant ou vide : {adapter}")
            raise DropItem("Missing name")
        
        return item
