# -*- coding:utf-8 -*-
from datetime import datetime
from myapps.pymongodb import dbconnection
from myapps.naver_crawling import naver_crawling
from myapps.daum_crawling import daum_crawling
from myapps.nate_crawling import nate_crawling
from myapps.crawling_db_input import crawling_db_input

#db입력 X
def crawlings():
    time = datetime.now()
    mydb = dbconnection()
    datas = {}
    datas["naver"] = naver_crawling(time, mydb)
    datas["daum"] = daum_crawling(time, mydb)
    datas["nate"] = nate_crawling(time, mydb)
    return datas

#db입력 O
def crawlings_db_input():
    time = datetime.now()
    mydb = dbconnection()
    datas = {}
    datas["naver"] = naver_crawling(time, mydb)
    crawling_db_input(time, mydb, datas["naver"], "naver")
    datas["daum"] = daum_crawling(time, mydb)
    crawling_db_input(time, mydb, datas["daum"], "daum")
    datas["nate"] = nate_crawling(time, mydb)
    crawling_db_input(time, mydb, datas["nate"], "nate")
    return datas