import requests
import os
from bs4 import BeautifulSoup
url='https://yandex.ru/images/search?text=tiger&lr=29388'
resp=requests.get(url).text
soup=BeautifulSoup(resp,'lxml')
resp1=soup.find_all("div",class_="serp-item")
b=1
for i in resp1:
    url_img=i.find("img",class_="serp-item__thumb justifier__thumb").get("src")
    print('https:' + url_img)
    
    img=requests.get('https:' + url_img).content
    a=str(b)
    ul='tiger/' + a + '.jpg'
    print(ul)
    if not os.path.isdir("tiger"):
        os.mkdir("tiger")
    with open(ul,'wb') as handler:
        handler.write(img)
    b=b+1