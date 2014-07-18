# -*- coding: utf-8 -*-
import scrapy

from ..items import BonnieItem


class JazzspiderSpider(scrapy.Spider):
    name = "jazzspider"
    allowed_domains = ["umbriajazz.com"]
    start_urls = (
        'http://www.umbriajazz.com/pagine/programma-umbria-jazz',
    )
    def parse(self, response):
        accordions = response.xpath("//div[@id='accordion']//ul//li")
        for accordion in accordions:
            date = accordion.xpath(".//h1/text()").extract()[0]

            indoor = accordion.xpath(".//table[1]")
            outdoor = accordion.xpath(".//table[2]")

            for row in indoor.xpath(".//tr"):
                concert = row.xpath(".//td").extract()
                time = concert[0]
                description = concert[1]

                #Filling item
                item = BonnieItem()
                item['datetime'] = "%s %s" % (date, time)
                item['description'] = description 
                item['outdoor'] = False

                yield item 
                
