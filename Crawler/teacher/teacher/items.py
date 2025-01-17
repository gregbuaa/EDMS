# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TeacherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    name = scrapy.Field()
    uni = scrapy.Field()
    dep = scrapy.Field()
    pro = scrapy.Field()
    img_url = scrapy.Field()
    info_url = scrapy.Field()
