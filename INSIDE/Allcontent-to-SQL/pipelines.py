# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy_project4_2 import settings
import pymysql

class ScrapyProject42Pipeline:
        # ScrapyProject42Pipeline 的建構函數，用來與 MySQL 連接
        def __init__(self):
            self.connect = pymysql.connect(
                host=settings.MYSQL_HOST,
                db=settings.MYSQL_DATABASE,
                user=settings.MYSQL_USERNAME,
                passwd=settings.MYSQL_PASSWORD,
                charset='utf8'
            )
            self.cursor = self.connect.cursor()

        # Callback 函數，用來處理 item 元件
        def process_item(self, item, spider):
            sql = 'INSERT INTO posts(post_title, post_date, post_author, post_essay)VALUES(%s,%s,%s,%s) '
            data = (item['post_title'], item['post_date'], item['post_author'], item['post_essay'])
            self.cursor.execute(sql, data)
            return item

        # 當 Spider 結束時，關閉與資料庫的連練
        def close_spider(self, spider):
            self.connect.commit()
            self.connect.close()
