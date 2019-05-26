# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

def naver_crawling(time, mydb):
    html = requests.get('https://www.naver.com/').text
    soup = BeautifulSoup(html, 'html.parser')
    spans = soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')
    index = 0
    title_list = []
    for span in spans:
        index += 1
        title_list.append({'key':index, 'value':span.text})
    return title_list
