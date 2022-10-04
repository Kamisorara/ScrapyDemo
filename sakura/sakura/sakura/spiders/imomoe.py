import scrapy
from sakura.items import SakuraItem


class ImomoeSpider(scrapy.Spider):
    name = 'imomoe'
    allowed_domains = ['996dm.com']
    start_urls = ['http://www.996dm.com']

    def parse(self, response):
        for i in range(1, 127):
            nextPage = "http://www.996dm.com/type/ribendongman-{}.html".format(i)
            yield scrapy.Request(url=nextPage, callback=self.parse_imomoe)

    def parse_imomoe(self, response):
        AnimationItemLists = response.xpath('//ul[@class="stui-vodlist clearfix"]/li')
        # print(AnimationItemLists)
        for AnimationItem in AnimationItemLists:
            # 动漫标题
            title = AnimationItem.xpath('.//div[1]/a/@title').extract_first()
            # 动漫描述
            describe = AnimationItem.xpath('.//div[1]/div[1]/p/text()').extract_first()
            # 动漫封面链接
            img_url = AnimationItem.xpath('.//div[1]/a/@data-original').extract_first()
            # print(title,describe,img_url)
            Animation = SakuraItem(title=title,
                                   describe=describe,
                                   img_url=img_url)
            yield Animation
