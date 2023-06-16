import random
import sys
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import requests
from PIL import Image
import pillow_avif


def get_image(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.1.4031 SLBChan/10'}

        response = requests.get(
            url,
            headers=headers)
        if (response.status_code == 200):
            return response.content
    except Exception as e:
        print(e)



f = open('data.csv', mode='w', encoding='utf-8-sig', newline='')

csv_writer = csv.DictWriter(f, fieldnames=[
    'id',
    'shop',
    'image',
    'title',
    'kind',
    'price',
    'count',
    'repertory'
])
csv_writer.writeheader()

file = "D:\download\google\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome()

kinds = ['手机', '电脑', '男装', '女装', '美食', '书籍', '家用', '实用']

dataIndex = 1
imgIndex = 1
kindIndex = 1
index = 1
dataIndex2 = 1
flag = True
for i in kinds:
    flag = True
    driver.get("https://www.jd.com")
    driver.find_element("id", "key").clear()
    driver.find_element("id", "key").send_keys(i)
    driver.find_element("id", "key").send_keys(Keys.ENTER)

    driver.implicitly_wait(10)

    lis = driver.find_elements_by_css_selector(".gl-item")

    print(lis)
    print(len(lis))
    while len(lis) < 30:
        driver.close()
        driver = webdriver.Chrome()
        driver.get("https://www.jd.com")
        driver.find_element("id", "key").clear()
        driver.find_element("id", "key").send_keys(i)
        driver.find_element("id", "key").send_keys(Keys.ENTER)
        driver.implicitly_wait(10)

        lis = driver.find_elements_by_css_selector(".gl-item")
    imgs = []

    for li in lis:
        id = dataIndex
        shop = li.find_element_by_css_selector(".p-shop a").text
        image = "goods/" + str(dataIndex) + ".jpg"
        title = li.find_element_by_css_selector(".p-name em").text
        kind = kindIndex
        price = li.find_element_by_css_selector(".p-price i").text
        count = random.randint(10, 1000000)
        repertory = random.randint(10, 1000)
        img = li.find_element_by_css_selector(".p-img img").get_attribute('src')
        if img is None:
            img = str(li.find_element_by_css_selector(".p-img img").get_attribute('data-lazy-img'))
            img = img.replace("//", 'https://')
        imgs.append(img)
        dataIndex += 1

        dit = {
            'id': id,
            'shop': shop,
            'image': image,
            'title': title,
            'kind': kind,
            'price': price,
            'count': count,
            'repertory': repertory
        }
        csv_writer.writerow(dit)

    print(imgs)

    for i in imgs:
        fileName = "goods/" + str(imgIndex) + '.jpg'
        if('avif' in i):
            fileName = str(imgIndex) + '.avif'
        fp = open(fileName, 'wb')
        image = get_image(i)
        error = 1
        while image is None:
            print(image)
            print("重试: " + str(error))
            sleep(10)
            image = get_image(i)
            error += 1
        fp.write(image)
        fp.close()
        if ('avif' in i):
            flag = True
            i = 1
            avifImage = ''
            while i > 0:
                try:
                    avifImage = Image.open(fileName)
                except Exception as e:
                    i += 1
                    print(e)
                i -= 1
            avifImage.save("goods/" + fileName.replace('avif', 'jpg'), 'jpeg')
        imgIndex += 1
        print("已完成：" + str(index))
        index += 1
    kindIndex += 1
f.close()
