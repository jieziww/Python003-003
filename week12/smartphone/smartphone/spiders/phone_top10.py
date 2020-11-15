import scrapy
from smartphone.items import SmartphoneItem
from smartphone.items import SmartphoneCommentsItem
from snownlp import SnowNLP


class PhoneTop10Spider(scrapy.Spider):
    name = 'phone_top10'
    allowed_domains = ['smzdm.com']
    start_urls = [
        'https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/#feed-main/']

    def parse(self, response):
        phones = response.xpath(
            '//*[@id="feed-main-list"]/li[position()<11]/div/div[2]')
        phoneid = 0
        for phone in phones:
            phoneid += 1
            items = SmartphoneItem()
            items['title'] = phone.xpath('./h5/a/text()')[0].extract()
            items['zhi'] = phone.xpath(
                './div[@class="z-feed-foot"]/div[1]/span/a[1]/span[1]/span/text()')[0].extract()
            items['buzhi'] = phone.xpath(
                './div[@class="z-feed-foot"]/div[1]/span/a[2]/span[1]/span/text()')[0].extract()
            items['star'] = phone.xpath(
                './div[@class="z-feed-foot"]/div[1]/a[1]/span/text()')[0].extract()
            items['comment'] = phone.xpath(
                './div[@class="z-feed-foot"]/div[1]/a[2]/span/text()')[0].extract()
            items['url'] = phone.xpath('./h5/a/@href')[0].extract()
            items['hour'] = phone.xpath(
                './div[@class="z-feed-foot"]/div[2]/span/text()')[0].extract().replace('\t', '')
            yield items
            yield scrapy.Request(items['url'], callback=self.comments_parse, meta={'ID': phoneid})

    def comments_parse(self, response):
        ID = response.meta['ID']
        comment_list = response.xpath(
            '//div[@id="commentTabBlockNew"]//div[@class="comment_conBox"]/div[@class="comment_conWrap"]/div[1]/p/span')
        for comment in comment_list:
            items = SmartphoneCommentsItem()
            items['content'] = comment.xpath('./text()')[0].extract()
            items['mark'] = SnowNLP(items['content']).sentiments
            items['phoneid'] = ID
            yield items
        next_links = response.xpath(
            '//*[@id="commentTabBlockNew"]//li[@class="pagedown"]/a/@href').extract()
        if next_links and len(next_links) > 0:
            next_link = next_links[0]
            yield scrapy.Request(next_link, callback=self.comments_parse, meta={'ID': ID})
