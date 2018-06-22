#引入文件
import scrapy

class CourseItem(scrapy.Item):
    #课程标题
    title = scrapy.Field()
    #课程url
    url = scrapy.Field()
    #课程标题图片
    image_url = scrapy.Field()
    #课程描述
    introduction = scrapy.Field()
    #学习人数
    student = scrapy.Field()
    #图片地址
    image_path = scrapy.Field()