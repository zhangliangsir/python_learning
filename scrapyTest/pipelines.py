# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class TutorialPipeline(object):
    quotes_name = 'quotes'
    author_name = 'author'
    quotesInsert = '''insert into quotes(text,author,tags)
                        values('{text}','{author}','{tags}')'''
    authorInsert = '''insert into author(name,birthdate,bio)
                        values('{name}','{birthdate}','{bio}')'''

    def __init__(self, settings):
        self.settings = settings

    def process_item(self, item, spider):
        print(item)
        if spider.name == "quotes":
            sqltext = self.quotesInsert.format(
                text=pymysql.escape_string(item['text']),
                author=pymysql.escape_string(item['author']),
                tags=pymysql.escape_string(item['tags']))
            # spider.log(sqltext)
            self.cursor.execute(sqltext)
        elif spider.name == "author":
            sqltext = self.authorInsert.format(
                name=pymysql.escape_string(item['name']),
                birthdate=pymysql.escape_string(item['birthdate']),
                bio=pymysql.escape_string(item['bio']))
            # spider.log(sqltext)
            self.cursor.execute(sqltext)
        else:
            spider.log('Undefined name: %s' % spider.name)

        return item

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def open_spider(self, spider):
        # 连接数据库
        self.connect = pymysql.connect(
            host=self.settings.get('MYSQL_HOST'),
            port=self.settings.get('MYSQL_PORT'),
            db=self.settings.get('MYSQL_DBNAME'),
            user=self.settings.get('MYSQL_USER'),
            passwd=self.settings.get('MYSQL_PASSWD'),
            charset='utf8',
            use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor();
        self.connect.autocommit(True)

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
