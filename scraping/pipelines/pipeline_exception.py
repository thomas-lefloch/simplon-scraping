from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class RequiredDataPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        required_fields = []
        for field_name, field in item.fields.items():
            if field.get("required", False):
                # si l'attribut n'existe pas, la valeur par "défaut" est False
                required_fields.append(field_name)

        for field_name in required_fields:
            if field_name not in adapter or not adapter[field_name]:
                spider.logger.warning(
                    f"[Info] Champ '{field_name}' manquant ou vide : {adapter}"
                )
                raise DropItem(f"Missing {field_name}")

        return item
