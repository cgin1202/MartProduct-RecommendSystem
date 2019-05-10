from pymongo import MongoClient

def dbconnection():
    username = 'tjans456'
    password = 'westdoor456'
    myclient = MongoClient('mongodb://%s:%s@54.180.81.132/westdoor456' %(username,password),27017)
    mydb = myclient["westdoor456"]
    return mydb
