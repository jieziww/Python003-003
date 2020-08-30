# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import CsvItemExporter
import pymysql
from scrapy.exceptions import DropItem

class SpidersPipeline:
    def __init__(self):
        self.file = open("./movies.csv","wb")
        self.exporter = CsvItemExporter(self.file)
        self.exporter.fields_to_export = ['title', 'category', 'release_date']
        self.exporter.start_exporting()

        try:
            self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='rj123',
                                          db='maoyan',
                                          charset='utf8mb4',)
        except Exception as e:
            raise DropItem(f'数据库连接异常： {e}')
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        self.exporter.export_item(item)

        try:
            sql = "INSERT INTO movies (title, category, release_date) VALUES (%s, %s, %s)"
            self.cursor.execute(sql, tuple(item.values()))
        except Exception as e:
            self.connection.rollback()
            print(f'数据库插入数据异常：{e}')
        return item

    def close_spider(self,spider):
        self.exporter.finish_exporting()
        self.file.close()
        try:
            self.cursor.close()
            self.connection.commit()
            self.connection.close()
        except Exception as e:
            raise DropItem(f'数据库异常： {e}')
