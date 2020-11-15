# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings
from smartphone.items import SmartphoneCommentsItem
from smartphone.items import SmartphoneItem


class SmartphonePipeline:
    def __init__(self):
        settings = get_project_settings()

        try:
            self.connection = pymysql.connect(host=settings.get('MYSQL_HOST'),
                                              user=settings.get('MYSQL_USER'),
                                              password=settings.get(
                                                  'MYSQL_PASSWORD'),
                                              db=settings.get('MYSQL_DBNAME'),
                                              charset=settings.get('MYSQL_CHARSET'),)
        except Exception as e:
            raise DropItem(f'数据库连接异常： {e}')
        self.cursor = self.connection.cursor()

        # 首先删除评论信息,由于设计外键信息,需要首先删除评论,便于更新评论信息
        try:
            sql = "TRUNCATE TABLE phone_comments"
            self.cursor.execute(sql)
        except Exception as e:
            self.connection.rollback()
            print(f'{sql} 异常：{e}')

        # 删除手机top信息,协助新的采集信息.
        try:
            sql = "TRUNCATE TABLE phone_top10"
            self.cursor.execute(sql)
        except Exception as e:
            self.connection.rollback()
            print(f'{sql} 异常：{e}')

    def process_item(self, item, spider):
        if isinstance(item, SmartphoneItem):
            try:
                sql = "INSERT INTO phone_top10 (title, zhi, buzhi, star, comment, url, hour) VALUES (%s,  %s, %s, %s, %s, %s, %s)"
                print(tuple(item.values()))
                self.cursor.execute(sql, tuple(item.values()))
            except Exception as e:
                self.connection.rollback()
                print(f'手机信息写入数据库异常：{e}')
            return item

        if isinstance(item, SmartphoneCommentsItem):
            try:
                sql = "INSERT INTO phone_comments (content, mark, phoneid) VALUES (%s, %s, %s)"
                self.cursor.execute(sql, tuple(item.values()))
            except Exception as e:
                self.connection.rollback()
                print(f"{item}评论信息写入数据库异常：{e}")
            return item

    def close_spider(self, spider):
        try:
            self.cursor.close()
            self.connection.commit()
            self.connection.close()
        except Exception as e:
            raise DropItem(f'数据库异常： {e}')
