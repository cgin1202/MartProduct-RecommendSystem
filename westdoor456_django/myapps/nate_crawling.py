# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from myapps.crawling_db_input import crawling_db_input

def nate_crawling(time, mydb):
    html = requests.get('https://search.daum.net/nate?q=&thr=sncc&w=tot/').text
    soup = BeautifulSoup(html, 'html.parser')
    title_list = soup.select('.content_realtime span[class*=keyword_rank]')
    return crawling_db_input(time, mydb, title_list, "nate")