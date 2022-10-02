# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter


class MystockPipeline:
    def open_spider(self, spider):  # 爬虫启动，对应的pipeline方法
        self.f = open('stocks.json', 'w', encoding="utf-8")  # 打开对应的文件

    # 下面这段代码就是写入的过程
    def process_item(self, item, spider):  # 核心部分，存储为文件
        self.f.write(str(item))
        return item

    def close_spider(self, spider):  # 爬虫关闭，对应的pipeline方法
        self.f.close()


# 加载settings里写的MYSQL配置文件
from scrapy.utils.project import get_project_settings


class mysqlPipline:
    def open_spider(self, spider):
        # DB_HOST = "192.168.31.250"
        # DB_PORT = 3306
        # DB_USER = "root"
        # DB_PASSWORD = "123456"
        # DB_NAME = "scrapyTest"
        # DB_CHARSET = "utf8mb4"
        settings = get_project_settings()
        self.host = settings["DB_HOST"]
        self.port = settings["DB_PORT"]
        self.user = settings["DB_USER"]
        self.password = settings["DB_PASSWORD"]
        self.name = settings["DB_NAME"]
        self.charset = settings["DB_CHARSET"]
        self.connect()

    def connect(self):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.name,
            charset=self.charset
        )

        self.corsor = self.conn.cursor()

    def process_item(self, item, spider):  # 核心部分，存储为文件

        # 具体执行插入的sql语句
        sql = 'INSERT INTO stocks ( `code`, abbreviation, marketValue, totalValue, LIQUI, generalCapital )VALUES("{}","{}","{}","{}","{}","{}")'.format(
            item["code"],
            item["abbreviation"],
            item["marketValue"],
            item["totalValue"],
            item["LIQUI"],
            item["generalCapital"])
        # 执行具体sql语句
        self.corsor.execute(sql)
        # 提交
        self.conn.commit()
        return item

    def close_spider(self, spider):
        # 关闭游标
        self.corsor.close()
        # 关闭连接
        self.conn.close()
