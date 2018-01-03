import scrapy

# 引入容器
from scrapytest.item.WaiHuiItems import WaiHuiItem


class MySpider(scrapy.Spider):
    # 设置name
    name = "HangQing"
    # 设定域名
    allowed_domains = ["http://finance.sina.com.cn"]
    # 填写爬取地址
    start_urls = ["http://finance.sina.com.cn/money/forex/hq/USDCNY.shtml"]

    # 编写爬取方法
    def parse(self, response):
        # 实例一个容器保存爬取的信息
        item = WaiHuiItem()
        # 这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
        # 先获取每个课程的div
        for box in response.xpath('//div[@id="quoteWrap"]'):
            # 获取每个div中的课程路径
            item['price'] = box.xpath('.//div/div[@class="price"]/h5').extract()[0].strip()[4:-5]
            item['name'] = "cnyusd"
            obj01 = box.xpath('.//div/ul[@class="change"]/li[@class="fontSmall"]')[0]
            item["time"] = obj01.select("text()")[0].extract()
            # 返回信息
            yield item
        print(111111111111111111111111111111111)
        url="http://finance.sina.com.cn/money/forex/hq/USDCNY.shtml"
        yield scrapy.Request(url, callback=self.parse)
        print(6666666666666666666666)
