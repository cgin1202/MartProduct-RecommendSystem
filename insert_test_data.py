#-*- coding:utf-8 -*-
import random
from pymongodb import dbconnection

mydb = dbconnection()
mycol = mydb["ratings"]
#print(mycol.find_one())
#print(mycol)

for id in range(1,1001):
    if(random.randrange(0,2) is 0):
        continue

    mydictionary = {"id":id, "item":{}}
    for itemindex in range(1, 71):
        if(random.randrange(0,10) is not 0):
            continue
        mydictionary["item"][str(itemindex)] = random.randrange(1, 50)
    print(mydictionary)
    x = mycol.insert_one(mydictionary)
    print(x.inserted_id)