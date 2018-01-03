import time
from scrapy.exceptions import IgnoreRequest
from scrapy.http import HtmlResponse, Response
from selenium import webdriver
import selenium.webdriver.support.ui as ui


class CustomDownloader(object):
    def __init__(self):
        # use any browser you wish
        cap = webdriver.DesiredCapabilities.PHANTOMJS
        cap["phantomjs.page.settings.resourceTimeout"] = 1000
        cap["phantomjs.page.settings.loadImages"] = True
        cap["phantomjs.page.settings.disk-cache"] = True
        self.driver = webdriver.PhantomJS()
        wait = ui.WebDriverWait(self.driver, 10)

    def VisitPersonPage(self, url):
        print('正在加载网站.....')
        self.driver.get(url)
        time.sleep(1)
        # 翻到底，详情加载
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        time.sleep(5)
        content = self.driver.page_source.encode('gbk', 'ignore')
        print('网页加载完毕.....')
        return content

    def __del__(self):
        self.driver.quit()


