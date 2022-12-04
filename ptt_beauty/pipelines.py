# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy_project9_ptt import settings
import pymysql
from scrapy.exporters import CsvItemExporter

# ImagesPipeline 相關
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request
# from scrapy import log


# 第一支爬蟲------------------ inside
class ScrapyProject9PttPipeline_inside:
    def process_item(self, item, spider):
        print('ScrapyProject9PttPipeline_inside','*'*100)
        print(item)
        pass

    # ScrapyProject9Pipeline 的建構函數，用來與 MySQL 連接
    '''
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
# CSS / MySQL 分開執行------------------

    # CSV 相關方法
    '''
    def __init__(self):
        self.file = open('class9_inside.csv', 'wb')
        self.exporter = CsvItemExporter(self.file, encoding='big5')
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
    '''


# 第二支爬蟲------------------ techorange

class ScrapyProject9PttPipeline_techorange:
    def process_item(self, item, spider):
        print('ScrapyProject9PttPipeline_techorange', '*' * 100)
        print(item)
        pass



class ScrapyProject9PttPipeline:
    def process_item(self, item, spider):
        return item









# ImagesPipeline 相關
class PttBeautyImgsPipeline(object):
    def process_item(self, item, spider):
        return item


class PttBeautyImgDownloadPipeline(ImagesPipeline):
    default_headers = {
        'accept': 'image/webp,image/*,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, sdch, br',
        'accept-language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'cookie': 'bid=yQdC/AzTaCw',
        'referer': 'https://www.douban.com/photos/photo/2370443040/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    }

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            self.default_headers['referer'] = image_url
            yield Request(image_url, headers=self.default_headers)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item
