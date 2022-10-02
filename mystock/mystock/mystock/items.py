# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MystockItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    code = scrapy.Field()  # 股票代码
    abbreviation = scrapy.Field()  # 股票简称
    marketValue = scrapy.Field()  # 流通市值(万元)
    totalValue = scrapy.Field()  # 总市值(万元)
    LIQUI = scrapy.Field()  # 流通股本(万元)
    generalCapital = scrapy.Field() #总股本(万元)