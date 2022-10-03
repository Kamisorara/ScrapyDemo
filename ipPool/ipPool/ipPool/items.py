# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IppoolItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 代理ip地址
    ip_addr = scrapy.Field()
    # 代理端口
    port = scrapy.Field()
    # 代理位置
    position = scrapy.Field()
