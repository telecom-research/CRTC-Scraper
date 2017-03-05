# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CrtcItem(scrapy.Item):
	metadata = scrapy.Field()
	content = scrapy.Field()
	pass

class FileItem(scrapy.Item):
	file = scrapy.Field()
	pass
    
class MetadataItem(scrapy.Item):   
    title = scrapy.Field()
    docType = scrapy.Field()
    keywords = scrapy.Field()
    subject = scrapy.Field()
    date = scrapy.Field()
    dateMod = scrapy.Field()
    dateIssued = scrapy.Field()
    dateCreated = scrapy.Field()
    pass

   
class ContentItem(scrapy.Item):
	pass
