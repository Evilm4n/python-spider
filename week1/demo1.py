from bs4 import BeautifulSoup

#/home/v5pingan/projectpy/week1/week1_demo
#/html/body/div/ul/li/a

with open('/home/v5pingan/projectpy/week1/week1_demo/demohtml.html','r') as wb_data:
    soup = BeautifulSoup(wb_data,'lxml')
    print(soup)