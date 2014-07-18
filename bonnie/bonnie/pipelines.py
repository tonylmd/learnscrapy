# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import bleach

class BonniePipeline(object):
    def strip_html(self, string):
        return bleach.clean(string, strip=True, tags=[])

    def strip_characters(self, string):
        return " ".join(string.split())

    def strip (self, string):
        return self.strip_characters(self.strip_html(string))

    def process_item(self, item, spider):
        item['datetime'] =  self.strip(item['datetime'])
        item['description'] =  self.strip(item['description'])
        return item
