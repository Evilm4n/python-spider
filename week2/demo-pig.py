from bs4 import BeautifulSoup
import requests
import time
import pymongo

'''
爬取小猪短租  1-3页数据
数据 = {
    '用户头像',
    '房子预览图',
    '标题',
    '地址',
    '价格',
}
'''
client = pymongo.MongoClient('localhost',27017)
xzData_db = client['xzData_db']
xz_tab = xzData_db['xz_tab']

urls = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i))for i in range(1,4)]
# url = 'http://bj.xiaozhu.com/search-duanzufang-p3-0/'

def get_info_xiaozhu(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    user_imgs = soup.select('img.landlordimage')
    imgs = soup.select('img.lodgeunitpic')
    prices = soup.select('span.result_price')
    room_sale_status = soup.select('span.room_status p.show')
    room_cates = soup.select('em.hiddenTxt')

    for user_img,img,price,room_sale_statu,room_cate in \
            zip(user_imgs,imgs,prices,room_sale_status,room_cates):
        data = {
            'user_img':user_img.get('lazy_src'),
            'title':img.get('title'),
            'img':img.get('lazy_src'),
            'price':price.get_text()[1:4],
            'room_sale_statu':room_sale_statu.get_text(),
            'room_cate' : [i.replace(' ', '').replace('\n','') for i in list(room_cate.stripped_strings)]
        }
        # xz_tab.insert(data)
        print(data)

for url in urls:
    time.sleep(2)
    get_info_xiaozhu(url)
    print('Done')

# for info in xz_tab.find({'price':{'$gt':'300'}}):
#     print(info)





