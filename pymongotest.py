from pymongodb import dbconnection

mydb = dbconnection()
product_no = int(mydb["camera"].find_one({"no":0})["product_no"])
mycol = mydb["customer"]
mycol.update({'no':11}, {'$inc':{'ratings.%d'%product_no:0.1}})

