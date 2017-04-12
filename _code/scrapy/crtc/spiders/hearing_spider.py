import scrapy
from crtc.items import HearingItem

class HearingSpider(scrapy.Spider):
	name = "hearing"
	download_delay = 5
	allowed_domains = ['www.crtc.gc.ca/eng/archive']
	start_urls = ["http://www.crtc.gc.ca/eng/transcripts/2016/tt0411.htm",
"http://www.crtc.gc.ca/eng/transcripts/2016/tt0412.htm",
"http://www.crtc.gc.ca/eng/transcripts/2016/tt0413.htm",
"http://www.crtc.gc.ca/eng/transcripts/2016/tt0414.htm",
"http://www.crtc.gc.ca/eng/transcripts/2016/tt0415.htm",
"http://www.crtc.gc.ca/eng/transcripts/2016/tt0418.htm",
"http://www.crtc.gc.ca/eng/transcripts/2016/tt0419.htm",
"http://www.crtc.gc.ca/eng/transcripts/2016/tt0420.htm",
"http://www.crtc.gc.ca/eng/transcripts/2016/tt0421.htm",
"http://www.crtc.gc.ca/eng/transcripts/2016/tt0422.htm",
"http://www.crtc.gc.ca/eng/transcripts/2016/tt0425.htm",
"http://www.crtc.gc.ca/eng/transcripts/2016/tt0426.htm",
"http://www.crtc.gc.ca/eng/transcripts/2016/tt0427.htm",
"http://www.crtc.gc.ca/eng/transcripts/2016/tt0428.htm"]

	def parse(self, response):
		sel = scrapy.Selector(response)
		page = response.url.split("/")[-1]
		file = page.split(".")[0] # creates a file name out of the url
		data = response.xpath('//head')
		webpage = []
		for d in data:
			item = HearingItem()
			item['title'] = d.xpath('//meta').re('\sname="dcterms.*itle"\scontent=\"(.*)\"')
			item['title'] = ''.join(item['title'])
			item['docType'] = d.xpath('//meta[@name="dcterms.type"]')[0].re('content="(.*)\"')
			item['docType'] = ''.join(item['docType'])
			item['subject'] = d.xpath('//meta[@name="dcterms.subject"]').re('title="gccrtcthes"\scontent="(.*)\"')
			item['subject'] = ''.join(item['subject'])
			item['dateIssued'] = d.xpath('//meta[@name="dcterms.issued"]').re('content="(\d{4}-\d{2}-\d{2})\"')
			item['dateIssued'] = ''.join(item['dateIssued'])
			item['url'] = response.request.url
			item['url'] = ''.join(item['url'])
			#item['attendees'] = d.xpath('//main/ul/li//text()').extract()
			#item['attendees'] = [x.replace("\r\n","") for x in item['attendees']]
			#item['attendees'] = [x for x in item['attendees'] if x]
			item['text'] = d.xpath('//main/*[not(contains(@class, "alert"))][not(contains(@lang, "fr"))]//text()[normalize-space()]').extract()
			webpage.append(item)
			return webpage