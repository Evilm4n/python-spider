from bs4 import BeautifulSoup
import requests
import time
import pymongo

client = pymongo.MongoClient('localhost',27017)
test = client['test']
url_list = test['url_list']
item_info = test['item_info']

#spider 1

def get_link_from(channel,pages,who_sells=0):
    #http://bj.58.com/diannao/0/pn3/
    list_view = '{}{}/pn{}/'.format(channel,str(who_sells),str(pages))
    wb_data = requests.get(list_view)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text,'lxml')
    if soup.find('td','t'):
        for link in soup.select('td.t a.t'):
            item_link = link.get('href').split('?')[0]
            url_list.insert_one({'url':item_link})
            print(item_link)
    else:
        pass

#get_link_from('http://bj.58.com/shuma/',20)

#spider 2

def get_item_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    no_longer_exist = '404' in soup.find('script',type="text/javascript").get('src').split('/')
    if no_longer_exist:
        pass
    else:
        title = soup.title.text
        price = soup.select('span.price.c_f50')[0].text
        date = soup.select('.time')[0].text
        area = list(soup.select('.c_25d a')[0].stripped_strings) if soup.find_all('span','c_25d') else None
        item_info.insert_one({'title':title,'price':price,'date':date,'area':area})
        print({'title':title,'price':price,'date':date,'area':area})

# get_item_info('http://bj.58.com/diannao/25194932476457x.shtml')