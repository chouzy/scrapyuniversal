# -*- coding: UTF-8 -*-
# @author: admin
# @createTime: 2022/7/25 11:32 
# @description:
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

rules = {
    'china': (Rule(LinkExtractor(allow=r'article\/.*\.html',
                                 restrict_xpaths='//div[@class="item-con-inner"]//h3[@class="tit"]/a'),
                   callback='parse_item', follow=True),
              Rule(LinkExtractor(restrict_xpaths='//div[@class="pages"]//a[contains(., "下一页")]')))
}
