# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 文本内容
    text = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 相关标签
    tags = scrapy.Field()
