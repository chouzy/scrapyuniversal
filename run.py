# -*- coding: UTF-8 -*-
# @author: admin
# @createTime: 2022/7/25 11:47 
# @description:
import sys
from scrapy.utils.project import get_project_settings
# from scrapyuniversal.spiders.universal import UniversalSpider
from scrapyuniversal.utils import get_config
from scrapy.crawler import CrawlerProcess


def run():
    name = sys.argv[1]
    custom_setting = get_config(name)
    # 爬取使用的 spider 名称
    spider = custom_setting.get('spider', 'universal')
    project_settings = get_project_settings()
    settings = dict(project_settings.copy())
    # 合并配置
    settings.update(custom_setting.get('settings'))
    process = CrawlerProcess(settings)
    # 启动爬虫
    process.crawl(spider, **{'name': name})
    process.start()


if __name__ == '__main__':
    run()
