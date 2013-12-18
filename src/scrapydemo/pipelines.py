# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class ScrapydemoPipeline(object):
    def process_item(self, item, spider):
        item['app_url'] = "http://www.appstar.com.cn" + item['app_url']
        return item
