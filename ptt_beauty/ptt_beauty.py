import scrapy
from scrapy.spiders import Spider
import re
from scrapy import Request
from ..items import PttBeautyImgsItem


class PttBeautySpider(scrapy.Spider):
    name = 'ptt_beauty'
    #allowed_domains = ['www.ptt.cc']
    #start_urls = ['https://www.ptt.cc/bbs/Beauty/M.1656293247.A.626.html']
    allowed_domains = ['buzzorange.com']
    start_urls = ['https://buzzorange.com/techorange/category/artificial-intelligence/']

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
    cookies = {'over18': '1'}  # 之前 request 用 cookies = {'over18':'1'}
    referer = {'https://www.douban.com/photos/photo/2370443040/'}


    def start_requests(self):
        for url in self.start_urls:
            #yield Request(url, headers=self.headers, cookies= self.cookies)
            yield Request(url, headers=self.headers,cookies=self.cookies,callback=self.parse)

    '''
    def img_inner(self, response):
        img_urls = response.xpath('//div[@class="col-md-6 col-sm-6 list-item"]//a/@href').getall()
        print(img_urls)
        for img_url in img_urls:
            yield Request(img_url, headers=self.headers, callback=self.parse)
    '''


    def parse(self, response):
        # ptt_beauty
        #list_imgs = response.xpath('//div[@class="bbs-screen bbs-content"]/a/text()').getall()

        # techorange 借用這隻spider 懶得再弄一支新的= =
        list_imgs = response.xpath('//img[@class="attachment-ceris-s-1_1 size-ceris-s-1_1 wp-post-image"]/@src').getall()
        print(list_imgs)
        if list_imgs:
            item = PttBeautyImgsItem()
            item['image_urls'] = list_imgs
            yield item