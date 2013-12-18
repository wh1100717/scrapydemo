from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapydemo.items import AppItem
class GroupSpider(CrawlSpider):
	name = "Group"
	allowed_domains = ["google.com"]
	start_urls = [
                "https://play.google.com/store/apps/details?id=com.tencent.mobileqq"
	]
	rules = [
		Rule(SgmlLinkExtractor(allow=('/apps/details\?id=', )),callback='parse_app')
	]
	def parse_app(self, response):	
		sel = Selector(response)
		items = []
		apps = sel.xpath("//a[@class='title']/@href")
		for app in apps:
                        item = AppItem()
			url = app.extract()
			item['app_url'] = url
                        items.append(item)
		return items
