# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from myapps.crawling_db_input import crawling_db_input

def naver_crawling(time, mydb):
    html = requests.get('https://www.naver.com/').text
    soup = BeautifulSoup(html, 'html.parser')
    spans = soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')
    index = 0
    title_list = []
    for span in spans:
        index += 1
        title_list.append({'key':index, 'value':span.text})
    crawling_db_input(time, mydb, title_list, "naver")
    return title_list
