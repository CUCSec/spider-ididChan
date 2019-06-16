import requests,re
import lxml
from bs4 import BeautifulSoup

def open_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'}
    response = requests.get(url = url, headers = headers)
    response.encoding = 'utf-8'
    html = response.text
    return html

def get_danmu_id(html):
    danmu_id = re.findall(r'cid=(\d+)&', html)[0]
    return danmu_id

video_url = f'https://www.bilibili.com/video/av54890746/'
video_html = open_url(video_url)

danmu_id = get_danmu_id(video_html)
danmu_url = 'https://api.bilibili.com/x/v1/dm/list.so?oid={}'.format(danmu_id)
danmu_html = open_url(danmu_url)

danmu_list = []
counter = 0

soup = BeautifulSoup(danmu_html, 'lxml')
all_d = soup.select('d')
for d in all_d:
    if(counter<=1000):
        danmu_list.append(d)
        counter += 1

with open('bilibili弹幕爬取'+'.txt','w+', encoding='utf8') as file:
    for i in danmu_list:
            file.write(str(i)+"\n")