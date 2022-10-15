# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter
from scrapy.utils.project import get_project_settings


class DoubanPipeline:
    def open_spider(self, spider):  # 爬虫启动，对应的pipeline方法
        self.f = open('stocks.json', 'w', encoding="utf-8")  # 打开对应的文件

    # 下面这段代码就是写入的过程
    def process_item(self, item, spider):  # 核心部分，存储为文件
        self.f.write(str(item))
        return item

    def close_spider(self, spider):  # 爬虫关闭，对应的pipeline方法
        self.f.close()


class mysqlPipline:
    def open_spider(self, spider):
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
        sql = 'INSERT INTO douban ( `rank`, `name`, `score`, `quote`,`img_url` )VALUES("{}","{}","{}","{}","{}")'.format(
            item["rank"],
            item["name"],
            item["score"],
            item["quote"],
            item["img_url"])

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



