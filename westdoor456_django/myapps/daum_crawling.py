# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from myapps.crawling_db_input import crawling_db_input

def daum_crawling(time, mydb):
    html = requests.get('http://www.daum.net/').text
    soup = BeautifulSoup(html, 'html.parser')
    title_list = soup.select('.hotissue_mini a[class*=link_issue]')
    return crawling_db_input(time, mydb, title_list, "daum")