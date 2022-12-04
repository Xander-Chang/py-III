import scrapy
from scrapy import Request

class InsideInnerContentSpider(scrapy.Spider):
    name = 'inside_inner_content'
    allowed_domains = ['www.inside.com.tw']
    start_urls = ['https://www.inside.com.tw/tag/ai']



    # request 加上標頭，偽裝成一般瀏覽器
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
    def start_requests(self):
        # 發出 Request 進行資料取得
        for url in self.start_urls:
            yield Request(url, headers=self.headers)  # headers = InsideInnerContentSpider.headers




    def parse(self, response):
        # 2022/06/01 新增，找到文章內容的所有連結
        post_urls = response.xpath("//a[@class='js-auto_break_title']/@href").getall()
        print(post_urls)

        # 2022/06/01 新增，針對所有文章發出 Request
        for post_url in post_urls:
            yield scrapy.Request(post_url, headers=self.headers, callback=self.parse_content)




    # 2022/06/01 新增，取得文章摘要內容
    def parse_content(self, response):
        # 文章介紹
        hot_news_title = response.xpath("//div[@class='post_introduction']/text()").get()

        print(f"文章介紹：{hot_news_title}")