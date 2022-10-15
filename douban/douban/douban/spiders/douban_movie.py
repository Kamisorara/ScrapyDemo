import scrapy
from douban.items import DoubanItem


class DoubanMovieSpider(scrapy.Spider):
    name = 'douban_movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com']

    def parse(self, response):
        for i in range(0, 25, 25):
            nextUrl = "https://movie.douban.com/top250?start={}&filter=".format(i)
            yield scrapy.Request(url=nextUrl, callback=self.parse_movie)

    def parse_movie(self, response):
        movieItemLists = response.xpath('//ol[@class="grid_view"]/li')
        for movieItem in movieItemLists:
            # 排名
            rank = movieItem.xpath('.//div/div[1]/em/text()').extract_first()
            # 电影名称(中文)
            name = movieItem.xpath('.//div/div[2]/div[1]/a/span[1]/text()').extract_first()
            # 评分
            score = movieItem.xpath('.//div/div[2]/div[2]/div/span[2]/text()').extract_first()
            # 引语
            quote = movieItem.xpath('.//div/div[2]/div[2]/p[2]/span/text()').extract_first()
            # 电影封面链接
            img_url = movieItem.xpath('.//div/div[1]/a/img/@src').extract_first()
            # 电影详情链接
            movieDetailUrl = movieItem.xpath('.//div/div[2]/div[1]/a/@href').extract_first()
            print(movieDetailUrl)

            yield scrapy.Request(url=movieDetailUrl, callback=self.movie_detail,
                                 meta={'rank': rank,
                                       'name': name,
                                       'score': score,
                                       'quote': quote,
                                       'img_url': img_url})

    def movie_detail(self, response):
        # 接受item
        rank = response.meta['rank']
        name = response.meta['name']
        score = response.meta['score']
        quote = response.meta['quote']
        img_url = response.meta['img_url']

        describe = response.xpath('//div[@id="link-report-intra"]/span[1]/span/text()').extract_first()
        # print(describe)
        movie = DoubanItem(rank=rank,
                           name=name,
                           score=score,
                           quote=quote,
                           img_url=img_url,
                           movie_describe=describe)
        yield movie
