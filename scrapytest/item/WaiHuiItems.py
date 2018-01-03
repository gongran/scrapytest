import scrapy


class WaiHuiItem(scrapy.Item):
    # 币种
    name = scrapy.Field()
    # 价格
    price = scrapy.Field()
    #时间
    time = scrapy.Field()
