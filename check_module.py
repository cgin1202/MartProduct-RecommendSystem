# -*- coding: utf-8 -*-
import cv2
import os
import sys
from cfr_module import cfr
from pydb import dbconnection
from time import sleep

def check():
    video_capture_0 = cv2.VideoCapture(0)
    while True:
        ret0, frame0 = video_capture_0.read()
        if(ret0):
            cv2.namedWindow('0',cv2.WINDOW_NORMAL)
            cv2.imshow('0', frame0)
            cv2.imwrite('images/0.jpg', frame0)

            if(cfr('images/0.jpg')['faces']!=[]):
                conn = dbconnection()
                curs = conn.cursor()
                sql = "INSERT INTO datas (client_id) VALUES (%s)"
                val = ("1111")
                curs.execute(sql, val)
                conn.commit()
                print("check")
            else:
                print('not checked')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

