# -*- coding:utf-8 -*-
from apyori import apriori
from pymongodb import dbconnection
def get_pattern(transactions, min_support, min_confidence):
    association_rules = apriori(transactions, min_support=min_support,  min_confidence=min_confidence)
    association_results = list(association_rules)
    result = []
    for association_result in association_results:
        for ass_result in association_result[2]:
            item_base = []
            for x in ass_result[0]:
                item_base.append(x)
            item_add = []
            for x in ass_result[1]:
                item_add.append(x)
            association = {}
            association["item_base"] = item_base 
            association["item_add"] = item_add
            association["confidence"] = ass_result[2]
            association["list"] = ass_result[3]
            result.append(association)
    return result


mydb = dbconnection()
mycol = mydb.dashboard_customer
datas = mycol.find()
transactions = []
product = ['라면', '사과', '피자', '버거', '세제', '감자', '만두', '삼겹살', '옥수수', '김']
for data in datas:
    intrans = []
    for key, value in data['customer_ratings'].items():
        if(int(value) != 0):
            intrans.append(product[int(key[-1:])])
    transactions.append(intrans)
#print(transactions)
patterns = get_pattern(transactions, 0.3, 0.7)
for pattern in patterns:
    print(pattern)
