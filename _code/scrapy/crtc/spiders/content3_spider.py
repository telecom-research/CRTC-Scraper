import scrapy
from crtc.items import CrtcItem, ContentItem

class Content3Spider(scrapy.Spider):
	name = "content3"
	download_delay = 10
	allowed_domains = ['www.crtc.gc.ca/eng/archive']
	start_urls = ['http://www.crtc.gc.ca/eng/archive/1997/DB97-477.htm', 'http://www.crtc.gc.ca/eng/archive/1997/DB97-626.htm',
'http://www.crtc.gc.ca/eng/archive/2017/2017-73.htm',
'http://www.crtc.gc.ca/eng/archive/2001/PT2001-99.htm',
'http://www.crtc.gc.ca/eng/archive/2005/db2005-362.htm',
'http://www.crtc.gc.ca/eng/archive/2011/2011-650.htm']
	
	def parse(self, response):
		sel = scrapy.Selector(response)
		page = response.url.split("/")[-1]
		file = page.split(".")[0] # creates a file name out of the url
		data = response.xpath('//head')
		webpage = []
		for d in data:
			item = ContentItem()
			item['file'] = file
			item['text'] = d.xpath('//main[contains(@property,"mainContentOfPage")]/*[not(contains(@id, "archived"))]//text()[normalize-space()]').extract() # grabs the body content, but excludes an archive paragraph
			item['text'] = ' '.join(list(map(str.strip,item['text']))) # strips the newlines and flattens the content into one string
			item['title'] = d.xpath('//meta').re('\sname="dcterms.*itle"\scontent=\"(.*)\"')
			item['title'] = ''.join(item['title'])
			item['docType'] = d.xpath('//meta[@name="dcterms.type"]')[0].re('content="(.*)\"')
			item['docType'] = ''.join(item['docType'])
			item['keywords'] = d.xpath('//meta[@name="keywords"]').re('content="(.*)\"')
			item['keywords'] = ''.join(item['keywords'])
			item['subject'] = d.xpath('//meta[@name="dcterms.subject"]').re('title="gccrtcthes"\scontent="(.*)\"')
			item['subject'] = ''.join(item['subject'])
			item['date'] = d.xpath('//meta[@name="dcterms.Date"]').re('content="(\d{4}-\d{2}-\d{2})\"')
			item['date'] = ''.join(item['date'])
			item['dateCreated'] = d.xpath('//meta[@name="dcterms.date.created"]').re('content="(\d{4}-\d{2}-\d{2})\"')
			item['dateCreated'] = ''.join(item['dateCreated'])
			item['dateIssued'] = d.xpath('//meta[@name="dcterms.issued"]').re('content="(\d{4}-\d{2}-\d{2})\"')
			item['dateIssued'] = ''.join(item['dateIssued'])
			item['dateMod'] = d.xpath('//meta[@name="dcterms.modified"]').re('content="(\d{4}-\d{2}-\d{2})\"')
			item['dateMod'] = ''.join(item['dateMod'])
			item['url'] = response.request.url
			item['url'] = ''.join(item['url'])
			webpage.append(item)
			return webpage
		
			
    		