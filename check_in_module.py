# -*- coding: utf-8 -*-
import cv2
import os
import sys
from pydb import dbconnection
from cfr_module import cfr

def check_in():
        video_capture_0 = cv2.VideoCapture(0)
        while True:
            ret0, frame0 = video_capture_0.read()

            if (ret0):
                cv2.namedWindow('0', cv2.WINDOW_NORMAL)
                cv2.imshow('0', frame0)
                cv2.imwrite('images/0.jpg', frame0)
                conn = dbconnection()
                curs = conn.cursor()
                if (cfr('images/0.jpg')["faces"] != []):
                    sql = "SELECT * FROM client WHERE id = %s"
                    val = ("1111")
                    curs.execute(sql, val)
                    rows = curs.fetchall()
                    print(rows)
                    if rows == ():
                        sql = "INSERT INTO client (id, gender, age, market_in) VALUES (%s,%s,%s,%s)"
                        val = ("1111", "M", "25", "1")
                        curs.execute(sql, val)
                        conn.commit()
                        print("enter")
                    else:
                        print("already entered")

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()
