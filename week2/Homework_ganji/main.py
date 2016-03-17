#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: v5pingan

from multiprocessing import Pool
from channel_lists import channel_urls_list
from page_parsing import get_url_list

# get all url_list

def get_all_list(channel):
    for num in range(1,101):
        get_url_list(channel, num)


if __name__ == '__main__':
    # 创建进程池
    pool = Pool()
    pool.map(get_all_list, channel_urls_list.split())