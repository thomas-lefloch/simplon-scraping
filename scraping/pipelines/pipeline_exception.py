from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class StripDataPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        for field_name, raw_data in adapter.items():
            if isinstance(raw_data, str):
                # Normalement à ce stade, toutes les données sont encore des str, mais...
                adapter[field_name] = raw_data.strip()

        return item


class RequiredDataPipeline:
    """
    Abandonne le traitement de l'objet si un champs requis est manquant.  
    Vous pouvez définir des champs requis en ajoutant la metadata "required=True"
    dans la définition de l'item.
    Exemple:  
    ```python
    class ItemCategories(scrapy.Item):  
        id = Field(required=True)  
    ```    
    Raises: DropItem: Si un champs requis est manquant
    """
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        required_fields = []
        for field_name, field in item.fields.items():
            if field.get("required", False):
                # si l'attribut n'existe pas, la valeur par "défaut" est False
                required_fields.append(field_name)

        for field_name in required_fields:
            if (
                field_name not in adapter
                or not adapter[field_name]
                or adapter[field_name] is None
            ):
                raise DropItem(
                    f"[Info] Champ '{field_name}' manquant ou vide : {adapter}"
                )

        return item


class TypeDataPipeline:
    """
    Abandonne le traitement de l'objet si un champs ne respecte pas le type définie par la metadata "value_type".  
    On essaye de convertir la valeur dans ce type avant d'abandonner le traitement.  
    Vous pouvez définir le type attendu de vos champs en utilisant la metadata "value_type"  
    dans la définition de l'item.  
    Exemple:   
    ```python
    class ItemProducts(scrapy.Item):
        base_price = Field(value_type=float) 
    ```    
    Raises: DropItem: Si un champs n'est pas conforme au type
    """
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
                        f"[Info] Champ '{field_name}' : impossible de convertir '{raw_value}' en {value_type.__name__}"
                    )

            # Temporaire pour sortie dan fichier de type texte (csv)
            # Formattage des floats avec 2 chiffres après le .
            if value_type == float and isinstance(adapter[field_name], float):
                adapter[field_name] = f"{adapter[field_name]:.2f}"

        return item
