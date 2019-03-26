# -*- coding: utf-8 -*-
import cv2
import os
import sys
from cfr_module import cfr
from pydb import dbconnection
from time import sleep
import face_recognition
import time

def face_catch(camera_no):
    video_capture_0 = cv2.VideoCapture(camera_no)
    start_vect=time.time()
    conn = dbconnection()
    curs = conn.cursor()
    sql = "SELECT id FROM client ORDER BY id DESC"
    curs.execute(sql)
    rows = curs.fetchall()
    name = int(rows[0][0])+1
    name = str(name)

    while True:
        ret0, frame0 = video_capture_0.read()
        if(ret0):
            cv2.namedWindow('0',cv2.WINDOW_NORMAL)
            cv2.imshow('0', frame0)
            if (time.time() - start_vect) > 5:
                cv2.imwrite('faces/0.jpg', frame0)
                res = cfr('faces/0.jpg')
                if res['faces']!=[] and res['faces'][0]['gender']['confidence'] >= 0.7:
                    gender = res['faces'][0]['gender']['value']
                    age = res['faces'][0]['age']['value']
                    ages = age.split('~')
                    print(ages)
                    age = (int(ages[0]) + int(ages[1]))/2
                    print(age)
                    age = res['faces'][0]['age']['value']
                    print('image detection complete!')
                    print(res['faces'][0]['gender']['confidence'])
                    cv2.imwrite('faces/'+name+'.jpg', frame0)
                    print("image saved!")
                    sql = "INSERT INTO client (id, gender, age, market_in, img_path) VALUES (%s,%s,%s,%s,%s)"
                    val = (name, gender, age, 1, name)
                    curs.execute(sql, val)
                    conn.commit()
                    print('db enter sucessful!')
                    break;
                else:
                    print("image detection failed, catch again")
                    start_vect=time.time()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

