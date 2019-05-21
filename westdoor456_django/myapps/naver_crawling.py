# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from myapps.crawling_db_input import crawling_db_input

def naver_crawling(time, mydb):
    html = requests.get('https://www.naver.com/').text
    soup = BeautifulSoup(html, 'html.parser')
    title_list = soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')
    return crawling_db_input(time, mydb, title_list, "naver")
