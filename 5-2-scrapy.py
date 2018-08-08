# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 22:55:15 2018

@author: LiJian
"""

import scrapy
import win32api

import pymongo

myclient = pymongo.MongoClient('localhost')

#创建数据库
mydb = myclient['MyDB']
dblist = myclient.database_names()
if "MyDB" in dblist:
    print("数据库已存在！")

#创建集合
mycol = mydb['sites']
collist = mydb.collection_names()
if "sites" in collist:   # 判断 sites 集合是否存在
  print("集合已存在！")

class MofanSpider(scrapy.Spider):
    name = "mofan"
    start_urls = [
        'https://morvanzhou.github.io/',
    ]
    # unseen = set()
    # seen = set()      # we don't need these two as scrapy will deal with them automatically

    def parse(self, response):
        yield {     # return some results
            'title': response.css('h1::text').extract_first(default='Missing').strip().replace('"', ""),
            'url': response.url,
        }
        # 往mongodb数据库存储爬取的数据
        yield mycol.insert_one({     # return some results
            'title': response.css('h1::text').extract_first(default='Missing').strip().replace('"', ""),
            'url': response.url,
        })
        urls = response.css('a::attr(href)').re(r'^/.+?/$')     # find all sub urls
        for url in urls:
            yield response.follow(url, callback=self.parse)     # it will filter duplication automatically


# lastly, run this in terminal
# scrapy runspider 5-2-scrapy.py -o res.json -s FEED_EXPORT_ENCODING=utf-8