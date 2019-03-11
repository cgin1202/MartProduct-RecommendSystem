import pymysql

def dbconnection():
    conn = pymysql.connect(host='nasosordss.cjf3pvz8picg.ap-northeast-2.rds.amazonaws.com', user='westdoor456', password='tjans456', db='westdoor456', charset='utf8')
    return conn 


