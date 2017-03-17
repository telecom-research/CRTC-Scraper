import scrapy
from crtc.items import CrtcItem, MetadataItem, FileItem, ContentItem

class Content3Spider(scrapy.Spider):
	name = "content3"
	download_delay = 5
	allowed_domains = ['www.crtc.gc.ca/eng/archive']
	start_urls = ['http://www.crtc.gc.ca/eng/archive/2017/2017-72.htm',
'http://www.crtc.gc.ca/eng/archive/2017/2017-73.htm',
'http://www.crtc.gc.ca/eng/archive/2017/2017-74.htm',
'http://www.crtc.gc.ca/eng/archive/2017/2017-8.htm',
'http://www.crtc.gc.ca/eng/archive/2017/2017-9.htm']
	
	def parse(self, response):
		sel = scrapy.Selector(response)
		page = response.url.split("/")[-1]
		file = page.split(".")[0]
		data = sel.xpath('//head')
		webpage = []
		for d in data:
			itemA = ContentItem()
			itemB = MetadataItem()
			itemB['title'] = d.xpath('//meta').re('\sname="dcterms.*itle"\scontent=\"(.*)\"')
			itemB['docType'] = d.xpath('//meta[@name="dcterms.type"]')[0].re('content="(.*)\"')
			itemB['keywords'] = d.xpath('//meta[@name="keywords"]').re('content="(.*)\"')
			itemB['subject'] = d.xpath('//meta[@name="dcterms.subject"]').re('title="gccrtcthes"\scontent="(.*)\"')
			itemB['date'] = d.xpath('//meta[@name="dcterms.Date"]').re('content="(\d{4}-\d{2}-\d{2})\"')
			itemB['dateCreated'] = d.xpath('//meta[@name="dcterms.date.created"]').re('content="(\d{4}-\d{2}-\d{2})\"')
			itemB['dateIssued'] = d.xpath('//meta[@name="dcterms.issued"]').re('content="(\d{4}-\d{2}-\d{2})\"')
			itemB['dateMod'] = d.xpath('//meta[@name="dcterms.modified"]').re('content="(\d{4}-\d{2}-\d{2})\"')
			itemC = CrtcItem()
			itemC['metadata'] = [dict(itemB)]
			itemC['content'] = [dict(itemA)]
			itemD = FileItem()
			itemD['file']= file, [dict(itemC)]
			webpage.append(itemD)
			return webpage
		
			
    		