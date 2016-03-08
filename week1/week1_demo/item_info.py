from bs4 import BeautifulSoup
import requests

url = 'http://bj.58.com/pingbandiannao/24063857671738x.shtml'

def get_item_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    date = soup.select('.time')[0].text
    data = {
        'title':soup.title.text,
        'date':soup.select('.time')[0].text,
        # 'price':soup.select('.price')[0].text,
        # 'area':list(soup.select('.c_25d')[0].stripped_strings) if soup.find_all('span .c_25d') else None,
        # 'cate':'个人' if who_sells == 0 else '商家',
        # 'views':get_views_from(url)
    }
    print(date)

get_item_info(url)