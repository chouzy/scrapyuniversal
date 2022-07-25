import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapyuniversal.items import NewsItem
from scrapyuniversal.loaders import ChinaLoader


class ChinaSpider(CrawlSpider):
    name = 'china'
    allowed_domains = ['tech.china.com']
    start_urls = ['http://tech.china.com/articles/']

    rules = (
        Rule(LinkExtractor(allow=r'article\/.*\.html',
                           restrict_xpaths='//div[@class="item-con-inner"]//h3[@class="tit"]/a'),
             callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//div[@class="pages"]//a[contains(., "下一页")]'))
    )

    # def parse_item(self, response):
    #     item = NewsItem()
    #     item['title'] = response.xpath('//*[@id="chan_newsTitle"]/text()').extract_first()
    #     item['url'] = response.url
    #     item['text'] = ''.join(response.xpath('//*[@id="chan_newsDetail"]/p/text()').extract()).strip()
    #     item['datetime'] = response.xpath('//*[@id="js-article-title"]/div[2]/span[1]/text()').re_first(
    #         r'(\d+-\d+-\d+\s\d+:\d+:\d+)')
    #     item['source'] = response.xpath('//*[@id="js-article-title"]/div[2]/span[2]/text()').re_first(
    #         r'来源：(.*)').strip()
    #     item['website'] = '中华网'
    #     # print(item)
    #     yield item

    def parse_item(self, response):
        loader = ChinaLoader(item=NewsItem(), response=response)
        loader.add_xpath('title', '//*[@id="chan_newsTitle"]/text()')
        loader.add_value('url', response.url)
        loader.add_xpath('text', '//*[@id="chan_newsDetail"]/p/text()')
        loader.add_xpath('datetime', '//*[@id="js-article-title"]/div[2]/span[1]/text()',
                         re=r'(\d+-\d+-\d+\s\d+:\d+:\d+)')
        loader.add_xpath('source', '//*[@id="js-article-title"]/div[2]/span[2]/text()', re=r'来源：(.*)')
        loader.add_value('website', '中华网')
        yield loader.load_item()
