# -*- coding: utf-8 -*-
import cv2
import os
import sys
import requests
import json

API_key='56bb3724ed1a7c7d6d8f4f067faec8c5'
client_id = "TdzD8AzvhVvaVq_7VHLi"
client_secret = "057fWaEVPl"
url =  "https://openapi.naver.com/v1/vision/face" # 얼굴감지
def CFR(cam_num):
    face = open(str(cam_num)+'.jpg','rb')
    files = {'image': face}
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
    response = requests.post(url,  files=files, headers=headers)
    rescode = response.status_code

    if(rescode==200):
        result = json.loads(response.text)
        print(result)
    else:
        print("Error Code:", rescode)

def show_webcam():
    video_capture_0 = cv2.VideoCapture(0)
    video_capture_1 = cv2.VideoCapture(1)
    while True:
        ret0, frame0 = video_capture_0.read()
        ret1, frame1 = video_capture_1.read()
        if(ret0):
            cv2.namedWindow('0',cv2.WINDOW_NORMAL)
            cv2.imshow('0', frame0)
            cv2.imwrite('0.jpg', frame0)
            CFR(0)
        if(ret1):
            cv2.namedWindow('1',cv2.WINDOW_NORMAL)
            cv2.imshow('1', frame1)
            cv2.imwrite('1.jpg', frame1)
            CFR(1)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

def main():
    show_webcam()
if __name__ == '__main__':
    main()
