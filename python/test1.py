import requests
import re

def get_html(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/111.0.0.0 Mobile Safari/537.36 Edg/111.0.1661.54'}

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.text

        return 0
    except:
        return "获取异常"

def re_html(html):

    pattern1 = '''<a.*?data-act="boarditem-click".*?>(.*?)</a>'''
    pattern2 = '''<p class="star">(.*?)</p>'''
    pattern3 = '''<p class="releasetime">(.*?)</p>'''
    pattern4 = '''(\S{8,})\\\\n'''

    name = re.findall(pattern1, html)
    star = re.findall(pattern2, html, re.S)
    star1 = re.findall(pattern4, str(star))
    time = re.findall(pattern3, html)

    return [name, star1, time]

url = "https://www.maoyan.com/board"

html = get_html(url)
info = re_html(html)

for i in range(0, len(info[0])):
    print("------------------------------------------")
    for j in range(0, len(info)):
        print(info[j][i])
    print("------------------------------------------")


