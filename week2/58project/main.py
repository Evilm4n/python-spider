#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: v5pingan

from multiprocessing import Pool
from channel_list import channel_url_list
from page_parsing import get_link_from

def get_all_link_from(channel):
    for num in range(1,101):
        get_link_from(channel,num)


if __name__ == '__main__':
    #创建进程池
    pool = Pool()
    pool.map(get_all_link_from,channel_url_list.split())

