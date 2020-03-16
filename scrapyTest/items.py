# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class TutorialItem(scrapy.Item):
    # for quotes
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
    # for author table
    name = scrapy.Field()
    birthdate = scrapy.Field()
    bio = scrapy.Field()
    
    