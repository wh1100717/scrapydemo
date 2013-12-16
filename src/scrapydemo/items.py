# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class AppItem(Item):
    # define the fields for your item here like:
    # name = Field()
    name = Field()
    cover = Field()

#    href = Field()
#    subtitle = Field()
#    description = Field()
#    price = Field()
#    author = Field()
#    lastUpdate = Field()
