import scrapy
from scrapy import Request


class TechorangeGooglesheetSpider(scrapy.Spider):
    name = 'techorange_googlesheet'
    allowed_domains = ['buzzorange.com']
    start_urls = ['https://buzzorange.com/techorange/category/artificial-intelligence/']



    # request 加上標頭，偽裝成一般瀏覽器
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
    def start_requests(self):
        # 發出 Request 進行資料取得
        for url in self.start_urls:
            yield Request(url, headers=self.headers)  # InsideGooglesheetSpider.headers



    def parse(self, response):
        yield from self.scrape(response)



    def scrape(self, response):

        post_title = response.xpath('//h3[@class="post__title typescale-2"]/a/text()').getall()
        post_date = response.xpath('//div[@class="post__meta"]/time[@class="time published"]/text()').getall()
        post_author = response.xpath('//div[@class="post__meta"]/a[@class="entry-author__name"]/text()').getall()


        for data in zip(post_title, post_date, post_author):
            ScrapyProject5GooglesheetItem = {
                'post_title': data[0],
                'post_date': data[1],
                'post_author': data[2]
            }
            yield ScrapyProject5GooglesheetItem

