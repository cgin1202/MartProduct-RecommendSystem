# -*- coding:utf-8 -*-
from myapps.pymongodb import dbconnection

def find_product(mycol, titlename):
    for x in mycol.find({},{"_id":0, "product_name":1}):
        #print(x['product_name'], titlename)
        if x['product_name'] in titlename or titlename in x['product_name']:
            return x['product_name']
    return 'false'