# -*- coding:utf-8 -*-
from myapps.find_product import find_product
def crawling_db_input(time, mydb, title_list, site):
    max_idx = len(title_list)
    for title in title_list:
        #print(title)
        calc = find_product(mydb.dashboard_product, title['value'])
        if(calc!='false'):
            doc = {'realtime_product':calc,'realtime_category': title['value'], 'realtime_site': site, 'realtime_ranking': title['key'], 'realtime_date': time, 'realtime_value':(max_idx-title['key']+1)/max_idx*10}
            mydb.dashboard_realtime.insert(doc)
