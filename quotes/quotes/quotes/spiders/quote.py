import scrapy
from quotes.items import QuotesItem


class QuoteSpider(scrapy.Spider):
    name = 'quote'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath('//div[@class="quote"]')
        for quote in quotes:
            text = quote.xpath('.//span[1]/text()').extract_first()
            author = quotes.xpath('.//span[2]/small/text()').extract_first()
            tags = quote.xpath('//div[@class="tags"]/a/text()').extract()
            # print(text, author, tags)
            quoteItem = QuotesItem(text=text,
                                   author=author,
                                   tags=tags)
            yield quoteItem

        next = response.xpath('//div[@class = "col-md-8"]/nav/ul/li[@class = "next"]/a/@href').extract_first()
        url = response.urljoin(next)
        yield scrapy.Request(url=url, callback=self.parse)
