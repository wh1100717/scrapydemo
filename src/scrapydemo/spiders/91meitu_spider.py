from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapy.http import Request

from scrapydemo.items import  ImgItem

class MeituSpider(BaseSpider):
    name = "91meitu"
    allowed_domains = ["91meitu.net"]
    start_urls = [
        "http://www.91meitu.net/"
    ]
    def parse(self, response):
        response_cookie = response.headers['Set-Cookie']
        for i in range(100):
            request = Request("http://www.91meitu.net/img-item/get-next?1&lastid=" + str((i+6)*10), callback=self.parse_request_page)
            request.headers['Cookie'] = response_cookie
            request.headers['Host'] = 'www.91meitu.net'
            request.headers['DK_AJAX_REQUEST'] = 'ajax-reqeust'
            yield request
        
    def parse_request_page(self, response):
        sel = Selector(response)
        imgboxes = sel.xpath("//div[@class='imgbox']")
        items = []
        for imgbox in imgboxes:
            item = ImgItem()
            item['url'] = imgbox.xpath("./img/@src").extract()[0]
            items.append(item)
        return items
        