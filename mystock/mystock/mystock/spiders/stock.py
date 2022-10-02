import scrapy
from mystock.items import MystockItem


class StockSpider(scrapy.Spider):
    name = 'stock'
    allowed_domains = ['quote.stockstar.com']
    start_urls = ['http://quote.stockstar.com/stock/industry_I_0_0_1.html']

    def parse(self, response):
        page = int(response.url.split("_")[-1].split(".")[0])  # 当前页码
        stockList = response.xpath('//tbody[@class="tbody_right"]/tr')  # 获取当前页面的股票列表
        for stock in stockList:
            code = stock.xpath('.//td[1]/a/text()').extract_first()  # 股票代码
            abbreviation = stock.xpath('.//td[2]/a/text()').extract_first()  # 股票简称
            marketValue = stock.xpath('.//td[3]/text()').extract_first()  # 流通市值(万元)
            totalValue = stock.xpath('.//td[4]/text()').extract_first()  # 总市值(万元)
            LIQUI = stock.xpath('.//td[5]/text()').extract_first()  # 流通股本(万元)
            generalCapital = stock.xpath('.//td[6]/text()').extract_first()  # 总股本(万元)
            # print(code, abbreviation, marketValue,totalValue) #可以打印一下
            stockItem = MystockItem(code=code,
                                    abbreviation=abbreviation,
                                    marketValue=marketValue,
                                    totalValue=totalValue,
                                    LIQUI=LIQUI,
                                    generalCapital=generalCapital)
            # 获取stockItem 交给piplines 处理
            yield stockItem

        # 通过检查后面网页的地址发现继续增加page的数量网页也会显示只是会显示“暂无数据!”
        Text = stockList[0].xpath('.//td/text()').extract_first()
        print(Text)
        if Text != "暂无数据!":  # 递归停止条件
            next_page = page + 1
            next_url = response.url.replace("{0}.html".format(page), "{0}.html".format(next_page))
            # 再回去调用Request方法 （Request就是scrapy的get请求）
            yield scrapy.Request(url=next_url, callback=self.parse)
