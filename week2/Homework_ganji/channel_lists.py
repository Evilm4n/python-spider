#coding"utf-8
from bs4 import BeautifulSoup
import requests

start_url = 'http://bj.ganji.com/wu/'

def get_channel_link(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')

    channel_list = soup.select('dl > dt > a[target="_blank"]')
    print(channel_list)

get_channel_link(start_url)