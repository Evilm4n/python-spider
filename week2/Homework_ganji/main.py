#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: v5pingan

from multiprocessing import Pool
from channel_lists import channel_urls_list
from page_parsing import get_url_list,item_info,url_list,get_item_info
import time

# 断点续爬
db_urls = [ url['url'] for url in url_list.find()]
index_urls = [ item['url'] for item in item_info.find()]
x = set(db_urls)
y = set(index_urls)
rest_urls = x-y


# get all url_list
def get_all_list(channel):
    for num in range(1,101):
        get_url_list(channel, num)


if __name__ == '__main__':
    # 创建进程池
    pool = Pool()
    pool.map(get_all_list, channel_urls_list.split())
    # time.sleep(2)
    # 爬取商品信息的 报错！
    # pool.map(get_item_info, rest_urls.split())



