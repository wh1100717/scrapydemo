from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapydemo.items import AppItem
from scrapy.http import Request
class GroupSpider(CrawlSpider):
	name = "appstar"
	allowed_domains = ["appstar.com.cn"]
	start_urls = [
                "http://www.appstar.com.cn/ace/store/26.htm"
	]
	
        def parse(self,response):
            for i in range(10):
                req = Request(url="http://www.appstar.com.cn/ace/store/"+str(i+26)+'.htm',callback = self.parse_app)
                yield req
                
	def parse_app(self, response):	
            sel = Selector(response)
            item= AppItem()
            item['app_url'] = sel.xpath("//*[@id='appDetail']/li[1]/a/@href").extract()[0]
            return item