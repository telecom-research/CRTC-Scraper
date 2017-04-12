# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CrtcItem(scrapy.Item):
	content = scrapy.Field()
	meta = scrapy.Field()
	pass

class ContentItem(scrapy.Item):
	text = scrapy.Field()
	title = scrapy.Field()
	docType = scrapy.Field()
	keywords = scrapy.Field()
	subject = scrapy.Field()
	date = scrapy.Field()
	dateMod = scrapy.Field()
	dateIssued = scrapy.Field()
	dateCreated = scrapy.Field()
	file = scrapy.Field()
	url = scrapy.Field()
	pass

class LinkScraperItem(scrapy.Item):
	url_from = scrapy.Field()
	url_to = scrapy.Field()
	
class HearingItem(scrapy.Item):
	title = scrapy.Field()
	docType = scrapy.Field()
	keywords = scrapy.Field()
	subject = scrapy.Field()
	date = scrapy.Field()
	dateMod = scrapy.Field()
	dateIssued = scrapy.Field()
	dateCreated = scrapy.Field()
	url = scrapy.Field()
	attendees = scrapy.Field()
	text = scrapy.Field()
	pass
