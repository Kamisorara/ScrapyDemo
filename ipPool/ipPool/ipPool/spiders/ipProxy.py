import scrapy
from ipPool.items import IppoolItem
import requests
import re


class IpproxySpider(scrapy.Spider):
    name = 'ipProxy'
    allowed_domains = ['www.89ip.cn']
    start_urls = ['https://www.89ip.cn']

    def parse(self, response):
        for i in range(1, 10):
            nextPage = "https://www.89ip.cn/index_{}.html".format(i)
            yield scrapy.Request(nextPage, callback=self.parse_ip)

    def parse_ip(self, response):

        ipItemList = response.xpath('//table[@class="layui-table"]/tbody/tr')
        for ipItem in ipItemList:
            ip_pattern = re.compile(r'\d+\.\d+\.\d+\.\d+')  # 简易版IP正则
            port_pattern = re.compile(r'\d+')  # 简易版port正则
            ip_addr = ipItem.xpath('.//td[1]/text()').extract_first()  # ip(未过滤)
            port = ipItem.xpath('.//td[2]/text()').extract_first()  # 端口（未过滤）
            position = ipItem.xpath('.//td[3]/text()').extract_first()  # 代理地址
            # print(ip_addr, port, position)
            # 清洗ip 和 port
            ip = ip_pattern.findall(str(ip_addr))[0]
            port = port_pattern.findall(str(port))[0]
            ipItems = IppoolItem(ip_addr=ip,
                                 port=port,
                                 position=position)
            if self.check_ip(ip, port):
                print(ip_addr + ' is valid')
                # 通过就入库
                yield ipItems
            else:
                print(ip_addr + ' is not valid')

    # 检查代理ip是否有效
    def check_ip(self, ip, port):
        url = 'http://icanhazip.com/'
        proxy = {'http': 'http://{}:{}'.format(ip, port)}
        try:
            r = requests.get(url, proxies=proxy, timeout=5)
            return r.text == ip
        except requests.exceptions.RequestException as e:
            return False
