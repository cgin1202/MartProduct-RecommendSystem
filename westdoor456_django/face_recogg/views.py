from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from myapps import face_recog
from myapps import pymongodb
from datetime import datetime

# Create your views here.
def gen(fr):
    mydb = pymongodb.dbconnection()
    fr.product_no = int(mydb["camera"].find_one({"no":fr.camera_no})["product_no"])
    mycol = mydb["customer"]
    camera_log = mydb["camera_log"]

    while True:
        jpg_bytes = fr.get_jpg_bytes(mycol)
        now_time = datetime.now()
        camera_log.insert_one({"camera_no":fr.camera_no, "product_no":fr.product_no, "customer_no":fr.now_no, "now_time":now_time})
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpg_bytes + b'\r\n\r\n')

def cam(request,no):
    return StreamingHttpResponse(gen(face_recog.FaceRecog(no)),content_type="multipart/x-mixed-replace;boundary=frame")

#def check(request, no):    