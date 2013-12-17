from scrapy.spider import BaseSpider
from scrapy.selector import Selector

from scrapydemo.items import AppItem

class GooglePlaySpider(BaseSpider):
    name = "google_play"
    allowed_domains = ["google.com"]
    start_urls = [
        "https://play.google.com/store/apps/collection/topselling_free"
    ]
    def parse(self, response):
        sel = Selector(response)
        items = []
        apps = sel.xpath("//div[@class='card no-rationale square-cover apps small']")
        for app in apps:
            item = AppItem()
            item['cover'] = app.xpath('div/div/div/div/div/img/@src').extract()[0]
            item['detail_page'] = app.xpath("div/div[@class='details']/a[@class='card-click-target']/@href").extract()[0]
            item['name'] = app.xpath("div/div[@class='details']/a[@class='title']/@title").extract()[0]
            item['company'] = app.xpath("div/div[@class='details']/div/a/@title").extract()[0]
            item['star_rating'] = app.xpath("div/div[@class='reason-set']/span/a/div/div/div/@style").extract()[0][7:-2]
            item['price'] = app.xpath("div/div[@class='reason-set']/span/span/span[2]/span[1]/span/text()").extract()[0]
            items.append(item)
        return items
    