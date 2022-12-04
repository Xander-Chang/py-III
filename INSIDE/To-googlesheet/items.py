# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyProject5GooglesheetItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 定義 inside.py 所要用的三個資料欄位
    post_title = scrapy.Field()
    post_date = scrapy.Field()
    post_author = scrapy.Field()