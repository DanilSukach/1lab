import requests
import os
from array import array
from bs4 import BeautifulSoup
from selenium import webdriver
import time

def scraping(url):
    if not os.path.isdir("dataset"):
        os.mkdir("dataset")
    if not os.path.isdir("dataset/" + url):
        os.mkdir("dataset/" + url)
    url_full="https://yandex.ru/images/search?text=" + url
    driver=webdriver.Chrome(executable_path='C:/Users/user/Desktop/1lab/chromedriver.exe')
    array=[]
    try:
        driver.get(url=url_full)
        time.sleep(2)
        for i in range(4):
            for i in range(10):
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                time.sleep(5)
            button=driver.find_element("class name","more__button")
            time.sleep(5)
            button.click()
            time.sleep(5)
        html=driver.page_source
        time.sleep(5)
        soup=BeautifulSoup(html,'lxml')
        resp_0=soup.find("div",class_="serp-list")
        index=0
        for i in range(1100):
            str_0=str(i)
            str_1='serp-item_pos_' + str_0
            resp_1=resp_0.find("div",class_=str_1)
            resp_2=resp_1.find("div",class_="serp-item__preview")
            resp_3=resp_2.find("a",class_="serp-item__link")
            url_img=resp_3.find("img",class_="serp-item__thumb justifier__thumb").get("src")
            if not url_img in array:
                array.append(url_img)
            else:
                break   
            print(array[i])
            img=requests.get('https:' + array[i]).content
            print(index)
            a=str(index)
            if index < 10:
                ul='dataset/' + url + '/' +'000'+ a + '.jpg'
            if 10 < index < 100:
                ul='dataset/' + url + '/' +'00'+ a + '.jpg'
            if 100 < index < 1000:
                ul='dataset/' + url + '/' +'0'+ a + '.jpg'
            if 1000 < index < 10000:
                ul='dataset/' + url + '/' + a + '.jpg'
            with open(ul,'wb') as handler:
                handler.write(img)
            index += 1
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

scraping("leopard")
scraping("tiger")

