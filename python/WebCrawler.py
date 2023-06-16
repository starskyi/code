import requests
import re

def get_html(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
            ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

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

''' def align(text, length):

    ch = 0
    en = 0
    for i in text:
        if '\u4e00' <= i <= '\u9fa5' and i > ascii(127) or i == '\uff1a':
            ch += 1
        else:
            en += 1
    al_len = ch*1.61 + en
    le = length - al_len
    if le > 0:
       for i in range(0, int(le)):
           print(" ", end='')
'''
url = "https://www.maoyan.com/board"

html = get_html(url)
info = re_html(html)

'''for i in range(0, len(info)):
    for k in range(0, len(info[0])):
        print("----------------------------------------", end='')
    print()
    for j in info[i]:
        print(j, end='')
        align(j, 40)
    if((i + 1) % 4 == 0):
        print()
'''

for i in range(0, len(info[0])):
    print("----------------------------------------------")
    #print('%-20s' % ())
    for j in range(0, len(info)):
        print(info[j][i])
    print("----------------------------------------------")


