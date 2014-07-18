# -*- coding: utf-8 -*-
import scrapy


class JazzspiderSpider(scrapy.Spider):
    name = "jazzspider"
    allowed_domains = ["umbriajazz.com"]
    start_urls = (
        'http://www.umbriajazz.com/pagine/programma-umbria-jazz',
    )

    def parse(self, response):
        accordion text = response.xpath("//div[@id='accordion'}//ul//li")
        print accordion text
        return
