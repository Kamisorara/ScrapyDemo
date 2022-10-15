# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # 排名
    rank = scrapy.Field()
    # 电影名称
    name = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 引语
    quote = scrapy.Field()
    # 电影封面链接
    img_url = scrapy.Field()
    # 电影详情介绍
    movie_describe = scrapy.Field()
