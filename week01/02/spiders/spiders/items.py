# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class SpidersItem(scrapy.Item):
    title = scrapy.Field()
    category = scrapy.Field()
    release_date = scrapy.Field()
