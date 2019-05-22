# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from myapps.crawling_db_input import crawling_db_input

def nate_crawling(time, mydb):
    html = requests.get('https://search.daum.net/nate?q=&thr=sncc&w=tot/').text
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('div', class_='wrap_rank')
    divs = table.find_all('div', class_='roll_rank')
    index = 0
    title_list = []
    for div in divs:
        index += 1
        item = div.find('div', class_='inner_item')
        data = item.find('a')
        title_list.append({'key':index, 'value':data.text})
    crawling_db_input(time, mydb, title_list, "nate")
    return title_list