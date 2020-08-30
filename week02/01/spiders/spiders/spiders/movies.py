import scrapy
from spiders.items import SpidersItem
from scrapy import Selector

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        sel = Selector(response=response)
        movies = sel.xpath('//div[contains(@class,"movie-hover-info")]')
        for movie in movies[:10]:
            items = SpidersItem()
            notes = movie.xpath('./div')
            items['title'] = notes[0].xpath('./span/text()').extract()
            items['category'] = notes[1].xpath('./text()')[1].extract().strip()
            items['release_date'] = notes[3].xpath('./text()')[1].extract().strip()
            yield items
