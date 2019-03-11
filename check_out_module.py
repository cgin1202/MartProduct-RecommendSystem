# -*- coding: utf-8 -*-
import cv2
import os
import sys
from pydb import dbconnection
from cfr_module import cfr

def check_out():
        video_capture_0 = cv2.VideoCapture(0)
        while True:
            ret0, frame0 = video_capture_0.read()

            if (ret0):
                cv2.namedWindow('0', cv2.WINDOW_NORMAL)
                cv2.imshow('0', frame0)
                cv2.imwrite('images/0.jpg', frame0)
                conn = dbconnection()
                curs = conn.cursor()
                if (cfr(0)["faces"] != []):
                    sql = "SELECT * FROM client"
                    curs.execute(sql)
                    rows = curs.fetchall()
                    print(rows)
                    if rows != ():
                        if rows[0][3] == 1:
                            sql = "UPDATE client SET market_in = %s WHERE id = %s"
                            val = ("0", "1111")
                            curs.execute(sql, val)
                            conn.commit()
                            print("change")
                        else:
                            print("you are not welcome")
                    else:
                        print("no person")

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()
