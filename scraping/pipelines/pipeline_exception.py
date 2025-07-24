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


class TypeDataPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        for field_name, field in item.fields.items():
            value_type = field.get("value_type", str)
            raw_value = adapter[field_name]

            if not isinstance(raw_value, value_type):
                try:
                    adapter[field_name] = value_type(raw_value)
                except (ValueError, TypeError) as e:
                    raise DropItem(
                        f"Champ '{field_name}' : impossible de convertir '{raw_value}' en {value_type.__name__}"
                    )

        return item
