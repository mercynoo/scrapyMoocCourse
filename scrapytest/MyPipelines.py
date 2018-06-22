#引入文件
from scrapy.exceptions import DropItem
import pymysql
from scrapytest import settings
import logging
import logging.config

import json

class MyPipeline(object):
    def __init__(self):
        #打开文件
        self.file = open('data.json', 'w', encoding='utf-8')
    #该方法用于处理数据
    def process_item(self, item, spider):
        #读取item中的数据
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        #写入文件
        self.file.write(line)
        #返回item
        return item
    #该方法在spider被开启时被调用。
    def open_spider(self, spider):
        pass
    #该方法在spider被关闭时被调用。
    def close_spider(self, spider):
        pass


class DBPipeline(object):

    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            port=3306,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor();

    def process_item(self, item, spider):
        try:
            # 查重处理
            self.cursor.execute(
                """select * from moocCourse where url = %s""",
                item['url'])
            # 是否有重复数据
            repetition = self.cursor.fetchone()

            # 重复
            if repetition:
                pass

            else:
                # 插入数据
                self.cursor.execute(
                    """insert into moocCourse(title, url, image_url, introduction, student)
                    value (%s, %s, %s, %s, %s)""",
                    (item['title'],
                     item['url'],
                     item['image_url'],
                     item['introduction'],
                     item['student']))

            # 提交sql语句
            self.connect.commit()

        except Exception as error:
            # 出现错误时打印错误日志
            logging(error)
        return item