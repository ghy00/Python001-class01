# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd


class MaoyanPipeline:
    # def process_item(self, item, spider):
    # return item

    def process_item(self, item, spider):

        title = item['title']
        types = item['types']
        times = item['times']
        with open('./movies.csv', 'a+', encoding='utf-8') as f:
            output = f'{title}\t{types}\t{times}\n\n'
            f.write(output)
        return item
