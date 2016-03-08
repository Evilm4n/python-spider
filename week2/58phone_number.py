from bs4 import BeautifulSoup
import requests
import pymongo

client = pymongo.MongoClient('localhost',27017)
phone_db = client['phone_db']
phone_tab = phone_db['phone_tab']

#单页

url = 'http://bj.58.com/shoujihao/'

wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')

number = soup.select('strong.number')
links = soup.select('a.t')

for num,link in zip(number,links):
    print(link.get('href'))


#http://jump.zhineng.58.com/clk?target=mv7V0A-b5HThmvqfpv--5yOdUAkhuA-1pyEqnHNzP1DOnWDOnHbQnjD1rH9LnHDvPWcvnHD1FMP_ULEqUA-1IAQ-uMEhuA-1IAYqnHEdP1nznHTvrj0QPiuzuymqpZwY0jCfsvFJsWN3shPfUiq1pAqdph-CmytfFMPfIgFWuHYQFMuG0LRGujYkFMuG0LRG0jYznWc8rj08nH0zsWckFhR8IZwk5HTh0A7zmyYqFh-1ug6YuyOb5yu6UZP-FMK_uWYVniuGUyRG5iudpyEqn1DdnjNdPWNLnjcQPHDhmvQopyEqrH93rj-6nvmVmHnYnBYYPvwbsycdnhEVPvubujc3P1bOnyc3FMKGujYYFhR8IA-b5HcdnWcYP1DOPjDvP1NQFhR8IZwk5HTh0ZFGmvNqPjbh0hRbpgcqpZwY0jCfsvFJsWN3shPfUiq1pAqdph-CmytfnWNznWELnHbYnHmLPH73sMPCIAd_FhwG0LKf01YQnBu1IyFGujYznHm1nHEYriuW0hR6IARb5HDLn1DOnHn1PjczrHcdPBukmgF6Uy-b5iubpgPWmHYzPjDh0vR_uhP65HcYniubpgP_U1YQFMP-UAu_U1YQFMDqniukmyI-UMRV5HDhmh-b5HEOFMIGUAwWmgFb5HThmgKkuyObpvROIvqzujYkFMF-mv7_UAu_UL0qnau6mMEqNE&psid=152719219191013987116626113&entinfo=25224719416751_0


