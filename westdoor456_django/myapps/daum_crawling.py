# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

def daum_crawling(time, mydb):
    html = requests.get('http://www.daum.net/').text
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select('.hotissue_mini a[class*=link_issue]')
    index = 0
    title_list = []
    for link in links:
        index += 1
        title_list.append({'key':index, 'value':link.text})
    return title_list
     