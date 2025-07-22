import csv
from itemadapter import ItemAdapter


class CsvWriterPipeline:
    def open_spider(self, spider):

        self.file = open(spider.name + ".csv", "w", newline="", encoding="utf-8")
        self.exporter = csv.writer(self.file)
        self.header_written = False

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        if not self.header_written:
            self.exporter.writerow(ItemAdapter(item).keys())
            self.header_written = True
        self.exporter.writerow(ItemAdapter(item).values())
        return item
