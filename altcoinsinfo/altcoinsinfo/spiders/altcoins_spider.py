import scrapy
from altcoinsinfo.items import AltcoinsinfoItem

class AltcoinsSpider(scrapy.Spider):

	name = 'altcoins'

	allowed_domains = ['coinmarketcap.com']
	start_urls = ['http://coinmarketcap.com/']

	def parse(self, response):
		for sel in response.xpath('//*[@id="currencies"]/tbody/tr'):
			item = AltcoinsinfoItem()
			item['rank'] = sel.xpath('td[1]/text()').extract()
			item['name'] = sel.xpath('td[2]/a/text()').extract()
			item['market_cap'] = sel.xpath('td[3]/text()').extract()
			# print item['rank'], item['name'], item['market_cap']
			yield item
