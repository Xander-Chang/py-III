import scrapy
from scrapy import Request


class InsideNextpageSpider(scrapy.Spider):
    name = 'inside_nextpage'
    allowed_domains = ['www.inside.com.tw']
    start_urls = ['https://www.inside.com.tw/tag/ai']



    # request 加上標頭，偽裝成一般瀏覽器
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
    def start_requests(self):
        # 發出 Request 進行資料取得
        for url in self.start_urls:
            yield Request(url, headers=self.headers)  # headers = InsideNextpageSpider.headers




    def parse(self, response):
        # 2022/06/01 新增，用 scrape 去取得網頁內容
        yield from self.scrape(response)

        # --------------------------------------------------------------------------------------------------------------
        # 2022/06/01 新增，定位「下一頁」按鈕元素
        next_page_url = response.xpath("//a[@class='pagination_item pagination_item-next']/@href")

        # 2022/06/01 新增，若有下一頁，則取得連結，繼續爬下一頁資料
        if next_page_url:
            url = next_page_url.get()  # 取得下一頁的網址
            yield Request(url, headers=self.headers, callback=self.parse)  # 發送請求
                               # headers = InsideNextpageSpider.headers
        # --------------------------------------------------------------------------------------------------------------




    def scrape(self, response):
        # 爬取文章標題 - XPath 方式
        post_titles = response.xpath("//a[@class='js-auto_break_title ']/text()").getall()
        # print(post_titles)

        # 爬取發佈日期 - XPath 方式
        post_dates = response.xpath("//li[@class='post_date']/span/text()").getall()
        # print(post_dates)

        # 爬取作者 - XPath 方式
        post_authors = response.xpath("//span[@class='post_author']/a/text()").getall()
        # print(post_authors)

        # print(zip(post_titles, post_dates, post_authors))

        # 將所取得的資料，用 zip 函數存成 tuple，並用 for 迴圈取出，建立 Item 內容
        for data in zip(post_titles, post_dates, post_authors):
            ScrapyProject4Item = {
                "post_title": data[0],
                "post_date": data[1],
                "post_author": data[2]
            }
            yield ScrapyProject4Item

