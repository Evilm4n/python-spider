#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: v5pingan

from bs4 import BeautifulSoup
import requests
import time
import pymongo

client = pymongo.MongoClient('localhost', 27017)
test = client['test']
url_list = test['url_list']
item_info = test['item_info']

# spider 1 抓取商品链接

def get_link_from(channel, pages, who_sells=0):
    # 完整的链接： http://bj.58.com/diannao/0/pn3/
    list_view = '{}{}/pn{}/'.format(channel, str(who_sells), str(pages))
    wb_data = requests.get(list_view)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    if soup.find('td', 't'):
        for link in soup.select('td.t a.t'):
            item_link = link.get('href').split('?')[0]
            if len(item_link) == 72:  # 判断去掉转转
                pass
            else:
                url_list.insert_one({'url': item_link})
                print(item_link)
    else:
        pass

# get_link_from('http://bj.58.com/shouji/', 10)

# spider 2 获取商品详情

def get_item_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    no_longer_exist = '404' in soup.find('script', type="text/javascript").get('src').split('/')
    if no_longer_exist:
        pass
    else:
        title = soup.title.text
        price = soup.select('span.price.c_f50')[0].text
        date = soup.select('.time')[0].text
        area = list(soup.select('#content > div.person_add_top.no_ident_top > div.per_ad_left > div.col_sub.sumary > ul \
        > li:nth-of-type(3) > div.su_con > span')[0].stripped_strings) if soup.find_all('span','c_25d') else None
        item_info.insert_one({'title':title,'price':price,'date':date,'area':area})
        print({'title': title, 'price': price, 'date': date, 'area': area})


# get_item_info('http://bj.58.com/shouji/25148656256462x.shtml')

