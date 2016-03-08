#coding:utf-8
from bs4 import BeautifulSoup
import requests
import time

url = 'https://cn.tripadvisor.com/Attractions-g60763-Activities-New_York_City_New_York.html'
url_saves = 'https://cn.tripadvisor.com/Saves#40993097'
urls = ['https://cn.tripadvisor.com/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html#ATTRACTION_LIST'.format(str(i)) for i in range(30,930,30)]
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/48.0.2564.116 Chrome/48.0.2564.116 Safari/537.36',
    'Cookie':'TASSK=enc%3Aau%2F2z4XErptBVErQGl4jn8MY9NcX5osABVwlwJXO4r%2BajsH%2BunK6sZYMgNVbEAXY0%2BQbDGL4T5c%3D; TAUnique=%1%enc%3A8xXkbySddZ7nN2dGOSNhsxbw%2BU6DtSd7KD7LsLWN3gp9i1%2B2aew%2BBQ%3D%3D; TAPD=cn.tripadvisor.com; ServerPool=X; WLRedir=requested; __gads=ID=6d1c936146a2d1e7:T=1456922515:S=ALNI_MbYa7Qk-tlK2KeGghh9phkrwQlu1A; SecureLogin2=3.3%3AtxP2O0VQoi418R3E%2FfYq4z2JybtELsCMQhCtTKgob9k8Fl9zgDh4NXyfURUObEYp0Gfh%2B8ess9SazekvI2UTStDNJlGII7%2FoGBIN28xmfFTbxnxKxP8rrDc6AUv3RzgcyGX9FOBJetJoCQZTo04y%2BnSXWgNziq1%2FGpXemI3cCqE%3D; TAAuth2=%1%3%3Aacc5de8fe813e70bfa550ed55024702a%3AAOqgiVE373kwyPx%2FzxYUnJFt7mOwpQYK64c5c9%2F0vVT9uE%2F0WXs41h7%2FKs3LsRHpcxU2ojc6EHRrkDH8iOaanMXDUlGCHRhM67hXL0iWorWUm4%2FpVbg4RxxocZeC9DlA3uamWDIoX%2FHHDubp70mU%2FN%2BdZF6mLdHzNJLlpoZfqbbcOj9nZWLspNnT3cAnWPjr0JRWG8CL6wnIAoxmIoMGbNw%3D; TATravelInfo=V2*AC.KWE*A.2*MG.-1*HP.2*FL.3*RVL.60763_62l105127_62l587661_62l105125_62l267031_62*RS.-1; TAReturnTo=%1%%2FAttraction_Review-g60763-d267031-Reviews-Manhattan_Skyline-New_York_City_New_York.html; roybatty=AAABUzeCRqe3YiKgnTm0e3Ok5z4AD%2FzsUY3Vew%3D%3D%2C1; CM=%1%HanaPersist%2C%2C-1%7Cpu_vr2%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7Cpu_vr1%2C%2C-1%7CFtrPers%2C%2C-1%7CHomeASess%2C1%2C-1%7CAWPUPers%2C%2C-1%7Ccatchsess%2C5%2C-1%7Cbrandsess%2C2%2C-1%7CCpmPopunder_1%2C1%2C1457011537%7CCCSess%2C%2C-1%7CCpmPopunder_2%2C1%2C-1%7Csesssticker%2C%2C-1%7C%24%2C%2C-1%7Ct4b-sc%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7Csess_rev%2C1%2C-1%7Csessamex%2C%2C-1%7CSaveFtrPers%2C%2C-1%7Cpers_rev%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C%2C-1%7CHomeAPers%2C%2C-1%7C+r_lf_1%2C%2C-1%7CRCSess%2C%2C-1%7C+r_lf_2%2C%2C-1%7Ccatchpers%2C3%2C1457527323%7CAWPUSess%2C%2C-1%7Cvr_npu2%2C%2C-1%7Csh%2C%2C-1%7CLastPopunderId%2C103-1655-39305%2C-1%7Cpssamex%2C%2C-1%7C2016sticksess%2C%2C-1%7Cvr_npu1%2C%2C-1%7CCCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cbrandpers%2C%2C-1%7C2016stickpers%2C%2C-1%7CWarPopunder_Session%2C%2C-1%7CWarPopunder_Persist%2C%2C-1%7Cr_ta_2%2C%2C-1%7Cr_ta_1%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; NPID=; TASession=%1%V2ID.E86329B7F9B61353CC77DCE5F9A21BEF*SQ.50*PR.427%7C*LS.UserReviewToDoListAjax*GR.82*TCPAR.44*TBR.71*EXEX.80*ABTR.33*PPRP.74*PHTB.14*FS.82*CPU.80*HS.popularity*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.7CFD52EF1A0320569B9894F73AE46878*FA.1*DF.0*LP.%2F*IR.1*OD.null*FBH.2*MS.-1*RMS.-1*FLO.60763*TRA.true*LL.972210*LD.105125*EWS.Attraction_Review; TAUD=LA-1456922481553-1*LG-2919604-2..F*LD-2919606-.....'
}

#获取首页栏目信息
def get_attr(url,data=None):
    wb_data = requests.get(url)#请求网页
    time.sleep(2)
    soup = BeautifulSoup(wb_data.text,'lxml')#解析网页，获取网页内容
    titles = soup.select('div.property_title > a[target="_blank"]')#爬取标题节点
    images = soup.select('img[width="160"]')#爬取图片节点
    cates  = soup.select('div.p13n_reasoning_v2')#爬取分类节点
    for title,img,cate in zip(titles,images,cates):#循环处理数据结构
        data = {
            'title':title.get_text(),
            'img':img.get('src'),
            'cate':list(cate.stripped_strings)
        }
        print(data)

#获取保存的栏目信息
def get_favs(url,data=None):
    wb_data = requests.get(url_saves,headers=headers)#添加头部信息请求网页
    soup = BeautifulSoup(wb_data.text,'lxml')#解析网页获取网页数据
    titles = soup.select('a.location-name')#爬取标题节点
    images = soup.select('img.photo_image')#爬取图片节点
    metas = soup.select('span.format_address')#爬取标签节点
    for title,img,meta in zip(titles,images,metas):#循环处理数据结构
        data = {
            'title':title.get_text(),
            'img':img.get('src'),
            'meta':list(meta.stripped_strings)
        }
        print(data)



for i_url in urls:
    get_attr(i_url)

