'''
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import BaseSpider, Rule
from scrapy.http import Request

DOMAIN = 'www.crtc.gc.ca/eng/dno.htm'
URL = 'http://%s' % DOMAIN

class LinkSpider(BaseSpider):
	name = DOMAIN
	download_delay = 5
	allowed_domains = [DOMAIN]
	start_urls = [URL]
	
	#rules = (Rule(LinkExtractor(allow=()), callback = 'parse', follow = True),)

	def parse(self, response):
		le = LinkExtractor(DOMAIN)
		for link in le.extract_links(response):
			#print(link.url)
			yield Request(link.url, callback=self.parse)
			
			
			#NOT WORKING
'''