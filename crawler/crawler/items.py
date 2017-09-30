# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MediaItem(scrapy.Item):
    """Item representing scraped media
    """
    url = scrapy.Field()
    media_type = scrapy.Field() # Article, Tweet, etc.
    references = scrapy.Field()
