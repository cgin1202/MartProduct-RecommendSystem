# -*- coding:utf-8 -*-
from myapps.find_product import find_product
def crawling_db_input(time, mydb, title_lists, site):
    max_idx = len(title_lists)
    lists = []
    for idx, title in enumerate(title_lists, 1):
        lists.append({'key':idx, 'value':title.text})
        calc=find_product(mydb.dashboard_product, str(title.text))
        if(calc!='false'):
            doc = {'realtime_product':calc,'realtime_category': str(title.text), 'realtime_site': site, 'realtime_ranking': idx, 'realtime_date': time, 'realtime_value':(max_idx-idx+1)/max_idx}
            mydb.dashboard_realtime.insert(doc)
    return lists