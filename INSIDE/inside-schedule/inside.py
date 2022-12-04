import scrapy


class InsideSpider(scrapy.Spider):
    name = 'inside'
    allowed_domains = ['www.inside.com.tw']
    start_urls = ['https://www.inside.com.tw/tag/ai']

    custom_settings = {'ITEM_PIPELINES': {'scrapy_project10.pipelines.ScrapyProject10Pipeline_inside': 300}}
    # request 加上標頭，偽裝成一般瀏覽器
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}



    def start_requests(self):
        # 發出 Request 進行資料取得
        for url in self.start_urls:
            yield scrapy.Request(url,
                          headers=self.headers)  # headers = InsideSpider.headers



    def parse(self, response):
        yield from self.parse_content(response)



    def parse_content(self, response):
        inside_title = response.xpath("//a[@class='js-auto_break_title ']/text()").getall()
        inside_date = response.xpath("//li[@class='post_date']/span/text()").getall()
        inside_author = response.xpath("//span[@class='post_author']/a/text()").getall()
        inside_essay = response.xpath("//p[@class='post_description js-auto_break_text']/text()").getall()

        for data in zip(inside_title, inside_date, inside_author, inside_essay):
            ScrapyProject10Item_inside = {
                "inside_title": data[0],
                "inside_date": data[1],
                "inside_author": data[2],
                "inside_essay": data[3]
            }
            yield ScrapyProject10Item_inside