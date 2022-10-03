# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter
from scrapy.utils.project import get_project_settings

class IppoolPipeline:
    def process_item(self, item, spider):
        return item


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
        sql = 'INSERT INTO ipProxy ( ip_addr, port, position )VALUES("{}","{}","{}")'.format(
            item["ip_addr"],
            item["port"],
            item["position"])
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