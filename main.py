import requests
import os
from array import array
from bs4 import BeautifulSoup
from selenium import webdriver
import time
url="https://yandex.ru/images/search?text=tiger"
driver=webdriver.Chrome(executable_path='C:/Users/user/Desktop/1lab/chromedriver.exe')
if not os.path.isdir("dataset"):
    os.mkdir("dataset")
if not os.path.isdir("dataset/leopard"):
    os.mkdir("dataset/leopard")
if not os.path.isdir("dataset/tiger"):
    os.mkdir("dataset/tiger")
array=[]
try:
    driver.get(url=url)
    time.sleep(2)
    for i in range(4):
        for i in range(10):
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            time.sleep(2)
        button=driver.find_element("class name","more__button")
        time.sleep(5)
        button.click()
        time.sleep(5)
    html = driver.page_source
    time.sleep(5)
    soup=BeautifulSoup(html,'lxml')
    resp1=soup.find("div",class_="serp-list")
    index=0
    for i in range(1100):
        s=str(i)
        s1='serp-item_pos_' + s
        resp2=resp1.find("div",class_=s1)
        resp3=resp2.find("div",class_="serp-item__preview")
        resp4=resp3.find("a",class_="serp-item__link")
        url_img=resp4.find("img",class_="serp-item__thumb justifier__thumb").get("src")
        if not url_img in array:
            array.append(url_img)
        else:
            break   
        print(array[i])
        img=requests.get('https:' + array[i]).content
        print(index)
        a=str(index)
        if index<10:
            ul='dataset/tiger/' +'000'+ a + '.jpg'
        if 10<index<100:
            ul='dataset/tiger/' +'00'+ a + '.jpg'
        if 100<index<1000:
            ul='dataset/tiger/' +'0'+ a + '.jpg'
        if 1000<index<10000:
            ul='dataset/tiger/' + a + '.jpg'
        with open(ul,'wb') as handler:
            handler.write(img)
        index=index+1
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

