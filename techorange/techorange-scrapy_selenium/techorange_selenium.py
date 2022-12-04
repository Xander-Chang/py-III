import scrapy
from scrapy_selenium import SeleniumRequest


class TechorangeSeleniumSpider(scrapy.Spider):
    name = 'techorange_selenium'
    allowed_domains = ['buzzorange.com']
    start_urls = ['https://buzzorange.com/techorange/category/artificial-intelligence/']



    header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
    def start_requests(self):
        yield SeleniumRequest(url='https://buzzorange.com/techorange/category/artificial-intelligence/', callback=self.parse)




    def parse(self, response):
        post_titles = response.xpath('//h3[@class="post__title typescale-2"]/a/text()').getall()
        post_dates = response.xpath('//time[@class="time published"]/text()').getall()
        post_authors = response.xpath("//a[@class='entry-author__name']/text()").getall()

        for data in zip(post_titles, post_dates, post_authors):
            ScrapyProject8Item = {
                'post_title': data[0],
                'post_date': data[1],
                'post_author': data[2]
            }
            yield ScrapyProject8Item
