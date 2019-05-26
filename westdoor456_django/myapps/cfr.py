# -*- coding: utf-8 -*-
import requests
import json


def cfr(image_path):
    API_key='56bb3724ed1a7c7d6d8f4f067faec8c5'
    client_id = "TdzD8AzvhVvaVq_7VHLi"
    client_secret = "057fWaEVPl"
    url =  "https://openapi.naver.com/v1/vision/face" # 얼굴감지
    
    face = open(image_path,'rb')
    files = {'image': face}
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
    response = requests.post(url,  files=files, headers=headers)
    rescode = response.status_code

    if(rescode==200):
        result = json.loads(response.text)
        return result
    else:
        return "Error Code:" + rescode
