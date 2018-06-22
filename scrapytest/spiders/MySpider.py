import scrapy
#引入容器
from scrapytest.CourseItems import CourseItem

class MySpider(scrapy.Spider):
    #设置name
    name = "MySpider"
    #设定域名
    allowed_domains = ["imooc.com"]
    #填写爬取地址
    start_urls = ["http://www.imooc.com/course/list"]
    #编写爬取方法
    def parse(self, response):
        #实例一个容器保存爬取的信息
        item = CourseItem()

        #先获取每个课程的div
        for box in response.xpath('//div[@class="course-card-container"]/a[@target="_blank"]'):
            #获取每个div中的课程路径
            item['url'] = 'http://www.imooc.com' + box.xpath('.//@href').extract()[0]
            # 获取div中的课程标题
            item['title'] = box.xpath('.//h3/text()').extract()[0].strip()
            #获取div中的标题图片地址
            item['image_url'] = "http:" + box.xpath('.//@src').extract()[0]
            #获取学生数量信息
            item['student'] = box.xpath('.//span/text()').extract()[0].strip()
            #获取div中的课程简介
            item['introduction'] = box.xpath('.//p/text()').extract()[0].strip()
            #返回信息
            yield item

        #url跟进开始
        #获取下一页的url信息
        url = response.xpath("//a[contains(text(),'下一页')]/@href").extract()
        if url :
            #将信息组合成下一页的url
            page = 'http://www.imooc.com' + url[0]
            #返回url
            yield scrapy.Request(page, callback=self.parse)
        #url跟进结束