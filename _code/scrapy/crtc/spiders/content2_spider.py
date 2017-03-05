import scrapy
from crtc.items import CrtcItem

class Content2Spider(scrapy.Spider):
	name = "content2"
	download_delay = 5
	allowed_domains = ['www.crtc.gc.ca/eng/archive']
	start_urls = ['http://www.crtc.gc.ca/eng/archive/2016/2016-491.htm', 'http://www.crtc.gc.ca/eng/archive/1997/DB97-1.htm', 'http://www.crtc.gc.ca/eng/archive/1998/C98-428.HTM']
		
		
	def parse(self, response):
		sel = scrapy.Selector(response)
		meta = sel.xpath('//head')
		metadata = []
		for m in meta:
			item = CrtcItem()
			item['number'] = m.xpath('//title').re('CRTC\s(\d*-\d*)[<\/title>|\W*<\/title>]')
			item['title'] = m.xpath('//meta').re('\sname="dcterms.*itle"\scontent=\"(.*)\"')
			item['docType'] = m.xpath('//meta[@name="dcterms.type"]')[0].re('content="(.*)\"')
			item['keywords'] = m.xpath('//meta[@name="keywords"]').re('content="(.*)\"')
			item['subject'] = m.xpath('//meta[@name="dcterms.subject"]').re('title="gccrtcthes"\scontent="(.*)\"')
			item['date'] = m.xpath('//meta[@name="dcterms.Date"]').re('content="(\d{4}-\d{2}-\d{2})\"')
			item['dateCreated'] = m.xpath('//meta[@name="dcterms.date.created"]').re('content="(\d{4}-\d{2}-\d{2})\"')
			item['dateIssued'] = m.xpath('//meta[@name="dcterms.issued"]').re('content="(\d{4}-\d{2}-\d{2})\"')
			item['dateMod'] = m.xpath('//meta[@name="dcterms.modified"]').re('content="(\d{4}-\d{2}-\d{2})\"')
			metadata.append(item)
			return metadata
		
			
    		