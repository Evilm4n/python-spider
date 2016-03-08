#coding:utf-8
from bs4 import BeautifulSoup
import requests

def get_links_from(who_sells=0): #获取列表的链接
    urls = []
    list_view = 'http://bj.58.com/pbdn/{}/pn2/'.format(str(who_sells))
    wb_data = requests.get(list_view)
    soup = BeautifulSoup(wb_data.text,'lxml')
    for link in soup.select('td.t a.t'):
        urls.append(link.get('href').split('?')[0])
    return urls
    # print(urls)

def get_views_from(url): #获取每条商品信息的浏览量
    id = url.split('/')[-1].strip('x.shtml')
    api = 'http://jst1.58.com/counter?infoid={}'.format(id)
    js = requests.get(api)
    views = js.text.split('=')[-1]
    # print(views)
    return views

def get_item_info(who_sells):#获取详情
    urls = get_links_from(who_sells)
    for url in urls:
        wb_data = requests.get(url)
        soup = BeautifulSoup(wb_data.text,'lxml')
        data = {
            'title':soup.title.text,
            'date':soup.select('.time')[0].text,
            'price':soup.select('.price')[0].text,
            'area':list(soup.select('.c_25d')[0].stripped_strings) if soup.find_all('span','c_25d') else None,
            'cate':'个人' if who_sells == 0 else '商家',
            'views':get_views_from(url)
        }
        print(data)

get_item_info(1)



'''
不知到为什么不能爬取个人的，下面是报错信息

File "/home/v5pingan/projectpy/week1/weekHomeWork/week1_58.py", line 33, in get_item_info
    'price':soup.select('.price')[0].text,
IndexError: list index out of range

'''