import scrapy
from scrapy_selenium import SeleniumRequest
from scrapy import Request


class InsideSeleniumSpider(scrapy.Spider):
    name = 'inside_selenium'
    allowed_domains = ['www.inside.com.tw']
    start_urls = ['https://www.inside.com.tw/tag/ai']



    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0',
               'referer': 'https://www.inside.com.tw'}
    def start_requests(self):
        yield SeleniumRequest(url='https://www.inside.com.tw/tag/ai', callback=self.parse)
        '''
        for url in self.start_urls:
        yield Request(url, headers=self.headers)
        '''




    def parse(self, response):
        post_titles = response.xpath('//a[@class="js-auto_break_title "]/text()').getall()

        for post_title in post_titles:
            print(post_title)

