#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: v5pingan

from bs4 import BeautifulSoup
import requests

start_url = 'http://bj.ganji.com/wu/'
url_host = 'http://bj.ganji.com'

def get_channel_link(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')

    channel_list = soup.select('dl > dt > a[target="_blank"]')
    for link in channel_list:
        urls_channel = url_host + link.get('href')
        print(urls_channel)

# get_channel_link(start_url)

channel_urls_list = '''
    http://bj.ganji.com/shouji/
    http://bj.ganji.com/shoujipeijian/
    http://bj.ganji.com/bijibendiannao/
    http://bj.ganji.com/taishidiannaozhengji/
    http://bj.ganji.com/diannaoyingjian/
    http://bj.ganji.com/wangluoshebei/
    http://bj.ganji.com/shumaxiangji/
    http://bj.ganji.com/youxiji/
    http://bj.ganji.com/xuniwupin/
    http://bj.ganji.com/jiaju/
    http://bj.ganji.com/jiadian/
    http://bj.ganji.com/zixingchemaimai/
    http://bj.ganji.com/rirongbaihuo/
    http://bj.ganji.com/yingyouyunfu/
    http://bj.ganji.com/fushixiaobaxuemao/
    http://bj.ganji.com/meironghuazhuang/
    http://bj.ganji.com/yundongqicai/
    http://bj.ganji.com/yueqi/
    http://bj.ganji.com/tushu/
    http://bj.ganji.com/bangongjiaju/
    http://bj.ganji.com/wujingongju/
    http://bj.ganji.com/nongyongpin/
    http://bj.ganji.com/xianzhilipin/
    http://bj.ganji.com/shoucangpin/
    http://bj.ganji.com/baojianpin/
    http://bj.ganji.com/laonianyongpin/
    http://bj.ganji.com/gou/
    http://bj.ganji.com/qitaxiaochong/
    http://bj.ganji.com/xiaofeika/
    http://bj.ganji.com/menpiao/
    http://bj.ganji.com/jiaju/
    http://bj.ganji.com/rirongbaihuo/
    http://bj.ganji.com/shouji/
    http://bj.ganji.com/shoujihaoma/
    http://bj.ganji.com/bangong/
    http://bj.ganji.com/nongyongpin/
    http://bj.ganji.com/jiadian/
    http://bj.ganji.com/ershoubijibendiannao/
    http://bj.ganji.com/ruanjiantushu/
    http://bj.ganji.com/yingyouyunfu/
    http://bj.ganji.com/diannao/
    http://bj.ganji.com/xianzhilipin/
    http://bj.ganji.com/fushixiaobaxuemao/
    http://bj.ganji.com/meironghuazhuang/
    http://bj.ganji.com/shuma/
    http://bj.ganji.com/laonianyongpin/
    http://bj.ganji.com/xuniwupin/
    http://bj.ganji.com/qitawupin/
    http://bj.ganji.com/ershoufree/
    http://bj.ganji.com/wupinjiaohuan/
'''