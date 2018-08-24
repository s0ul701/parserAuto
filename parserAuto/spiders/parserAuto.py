from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from parserAuto.items import ParserautoItem


class QuotesSpider(CrawlSpider):
    name = "parserAutoRu"
    start_urls = [
        'https://auto.ru/',
    ]
    allowed_domains = [
        'auto.ru',
    ]

    def parse_item(self, response):
        item = ParserautoItem()
        item['url'] = response.url
        yield item

    rules = (
        Rule(LinkExtractor(allow=[r'/\d+-\w+/$']), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=[r'^']), callback=None, follow=True)
    )
