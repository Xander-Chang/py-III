# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyProject10Item_inside(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    inside_title = scrapy.Field()
    inside_date = scrapy.Field()
    inside_author = scrapy.Field()
    inside_essay = scrapy.Field()

class ScrapyProject10Item_techorange(scrapy.Item):
    techorange_title = scrapy.Field()
    techorange_date = scrapy.Field()
    techorange_author = scrapy.Field()