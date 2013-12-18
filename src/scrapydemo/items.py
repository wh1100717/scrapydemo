# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class AppItem(Item):
    # define the fields for your item here like:
    # name = Field()
#    name = Field()
#    cover = Field()
#    detail_page = Field()
#    company = Field()
#    star_rating = Field()
#    price = Field()
    app_url = Field()
#    href = Field()
#    subtitle = Field()
#    description = Field()
#    price = Field()
#    author = Field()
#    lastUpdate = Field()

class ImgItem():
    url = Field()
