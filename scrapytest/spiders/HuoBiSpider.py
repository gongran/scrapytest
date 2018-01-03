import scrapy

from scrapytest.item.WaiHuiItems import WaiHuiItem


class HuoBiSpider(scrapy.Spider):
    name = "huobipro"
    allowed_domains = ["www.huobipro.com"]
    start_urls = [
        "https://www.huobipro.com/zh-cn/coin_coin/exchange/#btc_usdt"
        , "http://finance.sina.com.cn/money/forex/hq/USDCNY.shtml"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-1]
        box = response.xpath('//div[@id="quoteWrap"]')
        item = WaiHuiItem()
        if len(box) > 0:
            item['name'] = "cnyusd"
            price = box[0].xpath('.//div/div[@class="price"]/h5').extract()[0].strip()[4:-5]
            item['price'] = price
            yield item
        else:
            html = response.xpath("//div[@class='coin_filter']/span[@action='userfilter']")
            page = "https://www.huobipro.com/zh-cn/coin_coin/exchange/#btc_usdt"
            yield scrapy.Request(page, callback=self.parse)
            print(222)
