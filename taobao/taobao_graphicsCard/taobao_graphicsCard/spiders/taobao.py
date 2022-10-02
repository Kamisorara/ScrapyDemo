import scrapy
from taobao_graphicsCard.items import TaobaoGraphicscardItem


class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://search.dangdang.com']

    def parse(self, response):

        for i in range(1, 101):
            nextUrl = "http://search.dangdang.com/?key=Java&act=input&page_index={}".format(i)
            yield scrapy.Request(nextUrl, callback=self.parse_gc)

    def parse_gc(self, response):
        bookItemList = response.xpath('//div[@id="search_nature_rg"]/ul/li')
        for bookItem in bookItemList:
            title = bookItem.xpath('.//a/@title').extract_first()  # 标题
            image_url = bookItem.xpath('.//a/img/@data-original').extract_first()  # 图片链接
            price = bookItem.xpath('.//p[@class="price"]/span[1]/text()').extract_first()  # 价格
            # print(title, image_url, price)
            bookItems = TaobaoGraphicscardItem(title=title,
                                               image_url=image_url,
                                               price=price)
            yield bookItems
