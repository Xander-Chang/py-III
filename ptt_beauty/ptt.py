import scrapy, json, os
import pandas as pd

class PttSpider(scrapy.Spider):
    name = 'ptt'
    allowed_domains = ['www.ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/Gossiping/index.html']
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
    cookies = {'over18': '1'}  # 之前 request 用 cookies = {'over18':'1'}



    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.headers, cookies=self.cookies)



    def parse(self, response):
        # print(response.text)

        # 1. 標題
        ptt_titles = response.xpath('//div[@class="r-ent"]/div[@class="title"]/a/text()').getall()
        for ptt_title in ptt_titles:
            print(ptt_title, '*' * 60)
        #作者
        ptt_authors = response.xpath('//div[@class="meta"]/div[@class="author"]/text()').getall()
        for ptt_author in ptt_authors:
            print(ptt_author, '-.' * 60)
        #連結
        ptt_hrefs = response.xpath('//div[@class="r-ent"]/div[@class="title"]/a/@href').getall()
        for ptt_href in ptt_hrefs:
            print('https://www.ptt.cc/'+ ptt_href, '** ' * 60)
        #推文數
        ptt_pushs = response.xpath('//div[@class="r-ent"]/div[@class="nrec"]/span[@class="hl f2"]/text()').getall()
        for ptt_push in ptt_pushs:
            print(ptt_push, '*- ' * 60)
        # 2. 文章數量
        ptt_numbers = len(response.xpath('//div[@class="r-ent"]').getall())
        print(ptt_numbers, '=' * 60)

        # 3. 文章編號計數器
        # 4. 取得推文數量
        '''
        ptt_counts = 0
        for data in zip(ptt_titles, ptt_authors, ptt_hrefs, ptt_pushs):
            ptt_counts += 1
            ptt_dict= {
                '文章編號':ptt_counts,
                '標題':data[0],
                '作者':data[1],
                '連結':data[2],
                '推文數':data[3]
                }
            print(ptt_dict,'\n')
        '''

        # 5. 推文數大於某定值 (20) 推噓文








        # 6. 在上一層開新資料夾，把資料存 json檔案
        ptt_counts = 0
        ptt_dicts = []
        for data in zip(ptt_titles, ptt_authors, ptt_hrefs, ptt_pushs):
            ptt_counts += 1
            ptt_dicts.append({
                '文章編號': ptt_counts,
                '標題': data[0],
                '作者': data[1],
                '連結': data[2],
                '推文數': data[3]
            })

        if not os.path.exists('../ptt_json'):
            os.mkdir('../ptt_json')
        fullpath = os.path.join('../ptt_json','ptt_json.json')
        with open(fullpath,'w',encoding='utf-8') as f:
            json.dump(ptt_dicts, f, ensure_ascii=False, indent=2)





























