import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Spider, Rule
from scrapy.http import Request

DOMAIN = 'www.crtc.gc.ca/eng/dno.htm'
URL = 'http://%s' % DOMAIN

class LinkSpider(Spider):
	name = DOMAIN
	download_delay = 5
	allowed_domains = [DOMAIN]
	start_urls = [
		URL
    ]
	
	rules = (Rule(LinkExtractor(allow=(r'\/eng\/(\d{4}.*)')), callback = 'parse', follow = True),)
	
	def parse(self, response):
		hxs = scrapy.Selector(response)
		for url in hxs.xpath('//a/@href').extract():
			if not ( url.startswith('http://') or url.startswith('https://') ):
				url= 'http://www.crtc.gc.ca%s' % url 
				#print(url)
			yield Request(url, callback=self.parse)
		
		