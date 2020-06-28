# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd


class MaoyanPipeline(object):
    # def process_item(self, item, spider):
    # return item

    def process_item(self, item, spider):
        list1 = [(item['title'], item['types'], item['times'])]

        movie = pd.DataFrame(data=list1)
        movie.to_csv('./movie.csv', encoding='utf-8', index=False, header=False)
        return item
