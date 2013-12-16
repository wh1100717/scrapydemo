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
            item['cover'] = app.css('div[class=cover-inner-align] img::attr(src)').extract()
            item['name'] = app.css('div[class=details] a[class=title]::attr(title)').extract()[0]
            items.append(item)
        return items