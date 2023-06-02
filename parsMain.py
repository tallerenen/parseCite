import requests
from bs4 import BeautifulSoup
headers={'User-agent':
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)'}
f=open('new1.txt','w',encoding='utf-8')
url='https://shop.kz/catalog/?gclid=CjwKCAjwpayjBhAnEiwA-7ena-z0e4mSwZ5Qm2MbWTQOxt27E1cjaLaL-WVz2Ghd15fT7Jjg16R1kBoCj4IQAvD_BwE'
responce=requests.get(url,headers=headers)
# print(responce)
# print(responce.text)
soup=BeautifulSoup(responce.text,'lxml')
# print(soup)
data1=soup.find('div',class_='bx_catalog_tile')
data_li=data1.find_all('li')

ttpl = []

for i in data_li:
        data_text = i.find('h2')

        data_img = i.find('img').get('src')

        tuple = (data_text.text, 'https://shop.kz/' + data_img)
        ttpl.append(tuple)

print(ttpl)

def get():
        return ttpl