import scrapy

# 引入容器
from scrapytest.item.CourseItems import CourseItem


class MySpider(scrapy.Spider):
    # 设置name
    name = "MySpider"
    # 设定域名
    allowed_domains = ["imooc.com"]
    # 填写爬取地址
    start_urls = ["http://www.imooc.com/course/list"]

    # 编写爬取方法
    def parse(self, response):
        # 实例一个容器保存爬取的信息
        item = CourseItem()
        # 这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
        # 先获取每个课程的div
        for box in response.xpath('//div[@class="course-card-container"]/a[@target="_blank"]'):
            # 获取每个div中的课程路径
            item['url'] = 'http://www.imooc.com' + box.xpath('.//@href').extract()[0]
            # 获取div中的课程标题
            item['title'] = box.xpath('.//div[@class="course-label"]/label').extract()[0].strip()
            # 获取div中的标题图片地址
            item['image_url'] = box.xpath('.//@src').extract()[0]
            # 获取div中的学生人数
            item['student'] = box.xpath('.//span/text()').extract()[0].strip()[:-3]
            # 获取div中的课程简介
            item['introduction'] = box.xpath('.//p/text()').extract()[0].strip()
            # 返回信息
            yield item

        url = response.xpath("//a[contains(text(),'下一页')]/@href").extract()
        if url:
            # 将信息组合成下一页的url
            page = 'http://www.imooc.com' + url[0]
            # 返回url
            yield scrapy.Request(page, callback=self.parse)
            # url跟进结束
