# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from maoyan.items import MaoyanItem


class FilmSpider(scrapy.Spider):
    name = 'film'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):

        # 获取电影列表
        tags = Selector(response=response).xpath(
            '//div[@class="movie-item film-channel"]')

        for i in range(10):
            # 只取前10个电影
            tag = tags[i]

            # 获取电影名称
            title = tag.xpath(
                './/span[contains(@class,"name")]/text()').extract_first()

            # 获取上映时间、电影类型
            hover_texts = tag.xpath(
                './/span[@class="hover-tag"]/../text()').extract()
            # 通过xpath定位时多出了很多\n，数据索引有变化
            types = hover_texts[1].strip('\n').strip()
            times = hover_texts[5].strip('\n').strip()

            item = MaoyanItem()
            item['title'] = title
            item['types'] = types
            item['times'] = times

            yield item