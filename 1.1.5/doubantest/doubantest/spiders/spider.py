# -*- coding: utf-8 -*-
import scrapy


class Douban(scrapy.spiders.Spider):
    name = "doubanTest"
    start_urls = ['http://movie.douban.com/top250'
    ]
    def parse(self,response):
        print response.body
        print response.url
        a = response.url
        b = 1