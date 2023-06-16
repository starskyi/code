from time import sleep

import requests
import re

def get_html(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.1.4031 SLBChan/10'}

        response = requests.get(url, headers=headers)
        sleep(5)
        if response.status_code == 200:
            return response.text

        return 0
    except:
        return "获取异常"

# def re_html(html):
#
#     pattern1 = '''<a.*?data-act="boarditem-click".*?>(.*?)</a>'''
#     pattern2 = '''<p class="star">(.*?)</p>'''
#     pattern3 = '''<p class="releasetime">(.*?)</p>'''
#     pattern4 = '''(\S{8,})\\\\n'''
#
#     name = re.findall(pattern1, html)
#     star = re.findall(pattern2, html, re.S)
#     star1 = re.findall(pattern4, str(star))
#     time = re.findall(pattern3, html)
#
#     return [name, star1, time]

def re_html(html):
    imgPattern = '''<li.*?class="more2_item more2_item_good hover_on".*?>(.*?)</li>'''
    # return re.findall(imgPattern, html, re.S)
    return html


url = "https://www.jd.com/"

html = get_html(url)

info = re_html(html)


print(info)





