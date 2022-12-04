# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy_project8 import settings
import pymysql
from scrapy.exporters import CsvItemExporter



class ScrapyProject8Pipeline:
    '''
    # CSV 相關方法
    def __init__(self):
        self.file = open('class8_selenium_techorange_titles.csv', 'wb')
        self.exporter = CsvItemExporter(self.file, encoding='big5')
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()


# 存入 CSV / MySQL 只能選一個先後處理


    '''
    # ScrapyProject8Pipeline 的建構函數，用來與 MySQL 連接
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
        sql = 'INSERT INTO posts(post_title, post_date, post_author)VALUES(%s,%s,%s) '
        data = (item['post_title'], item['post_date'], item['post_author'])
        self.cursor.execute(sql, data)
        return item

    # 當 Spider 結束時，關閉與資料庫的連練
    def close_spider(self, spider):
        self.connect.commit()
        self.connect.close()
