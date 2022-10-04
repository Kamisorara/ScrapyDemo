# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SakuraItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    img_url = scrapy.Field()  # 图片链接
    title = scrapy.Field()  # 标题
    describe = scrapy.Field()  # 动漫描述
