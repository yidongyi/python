# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider

class My(CrawlSpider):
    name = "MyTest"
    start_urls = ['http://python.jobbole.com/86405/']
    def parse(self,response):
        print response.body
        print response.url
        a = response.url
        b = 1