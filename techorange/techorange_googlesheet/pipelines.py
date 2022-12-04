# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

# 將資料寫入 MySQL
from itemadapter import ItemAdapter
from scrapy_project5_googlesheet import settings
import pymysql

# 將資料寫入 Local CSV 檔案中
from scrapy.exporters import CsvItemExporter

# 將資料寫入 Google Sheet 中
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pkgutil



class ScrapyProject5GooglesheetPipeline:
    '''
    # ScrapyprojectPipeline 的建構函數，用來與 MySQL 連接
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
    '''



    '''
    # CSV 相關方法
    def __init__(self):
        self.file = open('posts.csv', 'wb')
        self.exporter = CsvItemExporter(self.file, encoding='big5')
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
    '''



    # 將資料寫入 Google Sheet
    def __init__(self):
        self.scopes = ["https://spreadsheets.google.com/feeds"]
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name("scrapy-project5-0568c74853e8.json", scopes=self.scopes)
        '''
        self.data = pkgutil.get_data("ScrapyProject", "resources/scrapy-352208-b1c442d6c7ea.json")
        self.data = self.data.decode("UTF-8")
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(self.data, scopes=self.scopes)
        self.credentials = ServiceAccountCredentials.from_json(json_data)
        '''
        self.client = gspread.authorize(self.credentials)
        self.sheet = self.client.open_by_key("1P_5hzECTB6BruBhDwcZfClIr4-1TK0h9ShVxH4lp2Sw").sheet1


    def process_item(self, item, spider):
        data = (item['post_title'], item['post_date'], item['post_author'])
        self.sheet.append_row(data)
        return item

    def close_spider(self, spider):
        # self.exporter.finish_exporting()
        # self.file.close()
        pass