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
    visited_urls = []
    cars_urls = []

    def parse_item(self, response):
        if response.url not in self.visited_urls:
            self.visited_urls.append(response.url)
            print("!!! " + response.url)
            # yield response.url

            # a = response.xpath('//div[@class="CardPhone-module__showPhoneText"]').extract()
            if response.url not in self.cars_urls:
                self.cars_urls.append(response.url)
                item = ParserautoItem()
                item['url'] = response.url
                yield item
        else:
            print('!!!!! CYCLE !!!!!')

    rules = (
        Rule(LinkExtractor(allow=[r'/\d+-\w+/$']), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=[r'^']), callback=None, follow=True)
    )
