import requests
import re


def get_image(keyword):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.1.4031 SLBChan/10'}

        response = requests.get(
            'https://search.jd.com/Search?keyword=' + keyword + '&enc=utf-8&wq=' + keyword,
            headers= headers)
        if (response.status_code == 200):
            return response.text
    except Exception as e:
        print(e)

reImg = '''<img .*? data-img="1" data-lazy-img="done" source-data-lazy-img src="(.*?).jpg">'''
html = get_image("手机")
data = re.findall(reImg, html, re.S | re.M)
print(data)


