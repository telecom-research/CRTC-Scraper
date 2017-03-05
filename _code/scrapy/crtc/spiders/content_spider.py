import scrapy


class ContentSpider(scrapy.Spider):
    name = "content"

    def start_requests(self):
    	urls = [
			'http://www.crtc.gc.ca/eng/archive/2016/2016-491.htm',
			'http://www.crtc.gc.ca/eng/archive/1997/DB97-1.htm',
		]
    	for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = '%s' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)