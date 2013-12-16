# Scrapy settings for scrapydemo project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scrapydemo'

SPIDER_MODULES = ['scrapydemo.spiders']
NEWSPIDER_MODULE = 'scrapydemo.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapydemo (+http://www.yourdomain.com)'
