# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SmartphoneItem(scrapy.Item):
    title = scrapy.Field()
    zhi = scrapy.Field()
    buzhi = scrapy.Field()
    star = scrapy.Field()
    comment = scrapy.Field()
    url = scrapy.Field()
    uuid = scrapy.Field()
    hour = scrapy.Field()


class SmartphoneCommentsItem(scrapy.Item):
    content = scrapy.Field()
    phoneid = scrapy.Field()
    mark = scrapy.Field()
