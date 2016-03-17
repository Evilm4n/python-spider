#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: v5pingan

from bs4 import BeautifulSoup
import requests
import time
import pymongo

client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
url_list = ganji['url_list']
item_info = ganji['item_info']

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
    'Cookie': 'statistics_clientid=me; citydomain=bj; ganji_xuuid=fc4cd584-4213-4903-eedb-3799b6812c2d.1458126440957; ganji_uuid=2579051618342869964887; GANJISESSID=fe6dca25de11c6b939b5709ac7d50529; hotPriceTip=1; __utmt=1; _gl_speed=%5B%22http%3A%2F%2Fwww.ganji.com%2Fuser%2Fthirdparty%2Fqq_login.php%3Fnext%3Dhttp%253A%252F%252Fbj.ganji.com%252Fshoujipeijian%252Fo2%252F%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22%2C1458130038336%5D; sscode=uP5nt5lplcEKchDvuPc6r5c%2F; GanjiUserName=%23qq_649860850; GanjiUserInfo=%7B%22user_id%22%3A649860850%2C%22email%22%3A%22%22%2C%22username%22%3A%22%23qq_649860850%22%2C%22user_name%22%3A%22%23qq_649860850%22%2C%22nickname%22%3A%22%5Cu96e8%5Cu5b63%5Cu3001%5Cu83ab%5Cu5fe7%5Cu79bb%5Cu2014%22%7D; bizs=%5B%5D; supercookie=AwD5BQLjBQHjWQNlMJZ5ZzAuMQAuZwV3LJRlZGqzMGMuAmR4LzV5BTMwZmZkAQH4BQV%3D; t3=2; lg=1; _gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A68841026464%7D; __utma=32156897.601174381.1458126441.1458126441.1458128641.2; __utmb=32156897.12.10.1458128641; __utmc=32156897; __utmz=32156897.1458126441.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

# spider1 爬去商品链接
def get_url_list(channel, pages, who_sells='o' ):
    # http://bj.ganji.com/shouji/o2/
    list_view = '{}{}{}/'.format(channel, who_sells, str(pages))
    wb_data = requests.get(list_view, headers=headers)
    time.sleep(2)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    if soup.find_all('a', 'prev'): #检测最后一页
        for link in soup.select('a.ft-tit'):
            if "zhuanzhuan" in link.get('href'):
                pass
            else:
                url_list.insert_one({'url': link.get('href')})
                print(link.get('href'))
    else:
        pass

# get_url_list('http://bj.ganji.com/shoujipeijian/', 200)

# spider 2  爬去商品信息
def get_item_info(url):
    wb_data = requests.get(url, headers=headers)
    time.sleep(2)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    if soup.find_all('p', 'error-tips1'):
        pass
    else:
        title = soup.title.text.split('-')[0]
        date = soup.select('.pr-5')[0].text.replace('发布','')
        type = soup.select('#wrapper > div.content.clearfix > div.leftBox > \
        div:nth-of-type(3) > div > ul > li:nth-of-type(1) > span > a')[0].text
        price = soup.select('.f22')[0].text
        address = list(soup.select('#wrapper > div.content.clearfix > div.leftBox > \
        div:nth-of-type(3) > div > ul > li:nth-of-type(3)')[0].stripped_strings)[1:]
        new_old = list(soup.select('#wrapper > div.content.clearfix > div.leftBox > \
        div:nth-of-type(4) > div.det-summary > div > div.second-dt-bewrite > ul > \
        li')[0].stripped_strings)[1:] if soup.find_all('ul','second-det-infor') else None
        data = {
            'title': title,
            'date': date,
            'type': type,
            'price': price,
            'address': address,
            'status': new_old
        }
        item_info.insert_one(data)
        print(data)


# get_item_info('http://bj.ganji.com/shouji/1883224957x.htm')