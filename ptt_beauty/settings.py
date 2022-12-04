# Scrapy settings for scrapy_project9_ptt project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapy_project9_ptt'

SPIDER_MODULES = ['scrapy_project9_ptt.spiders']
NEWSPIDER_MODULE = 'scrapy_project9_ptt.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_project9_ptt (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'scrapy_project9_ptt.middlewares.ScrapyProject9PttSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    #'scrapy_project9_ptt.middlewares.ScrapyProject9PttDownloaderMiddleware': 543,
    #'scrapy_project9_ptt.middlewares.RandomProxyMiddleware': 500,
    #'scrapy_project9_ptt.middlewares.SimpleProxyMiddleware': 100,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    #'scrapy_project9_ptt.pipelines.ScrapyProject9PttPipeline': 300,
    'scrapy_project9_ptt.pipelines.PttBeautyImgDownloadPipeline': 301,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'



# MySQL 相關設定
MYSQL_HOST = '127.0.0.1'
MYSQL_DATABASE = 'inside_techorange'
MYSQL_USERNAME = 'root'
MYSQL_PASSWORD = ''

# Selenium 相關設定
SELENIUM_DRIVER_NAME = 'chrome'  #瀏覽器名稱
SELENIUM_DRIVER_EXECUTABLE_PATH = 'chromedriver.exe'  #驅動程式路徑
SELENIUM_DRIVER_ARGUMENTS = ['-headless']

# 遇到錯誤時的相關設定
RETRY_ENABLED = True
RETRY_TIMES = 2  # initial response + 2 retries = 3 requests
RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408, 429]


# 设置图片下载路径
IMAGES_STORE = 'D:\_backup10\Desktop\聯成電腦\Python爬蟲程式開發(疫情期間，實體轉線上)陳信宏\Python爬蟲程式開發_012'
# 过期天数
IMAGES_EXPIRES = 90  #90天内抓取的都不会被重抓