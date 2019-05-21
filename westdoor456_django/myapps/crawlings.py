# -*- coding:utf-8 -*-
from datetime import datetime
from myapps.pymongodb import dbconnection
from myapps.naver_crawling import naver_crawling
from myapps.daum_crawling import daum_crawling
from myapps.nate_crawling import nate_crawling

def crawlings():
    time = datetime.now()
    mydb = dbconnection()
    datas = {}
    datas["naver"] = naver_crawling(time, mydb)
    datas["daum"] = daum_crawling(time, mydb)
    datas["nate"] = nate_crawling(time, mydb)
    return datas