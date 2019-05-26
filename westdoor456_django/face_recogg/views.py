from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from myapps import face_recog
from myapps import pymongodb
import time
from dashboard.models import CameraLog
from dashboard.models import Camera

# Create your views here.
def gen(fr, dbon):
    mydb = pymongodb.dbconnection()
    
    if(Camera.objects.get(camera_no=fr.camera_no).product):
        fr.product_no = Camera.objects.get(camera_no=fr.camera_no).product.product_no
    else:
        fr.product_no = -1
    mycol = mydb["dashboard_customer"]
    camera_log = mydb["camera_log"]
    nowtime = time.time()
    while True:
        jpg_bytes = fr.get_jpg_bytes(mycol, dbon)
        if (time.time() - nowtime >= 1) and dbon is True:
            nowtime = time.time()
            if fr.now_no != -2:
                CameraLog.objects.create(camera_id=int(fr.camera_no),customer_id=int(fr.now_no))
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpg_bytes + b'\r\n\r\n')

def cam(request,no):
    return StreamingHttpResponse(gen(face_recog.FaceRecog(no), False),content_type="multipart/x-mixed-replace;boundary=frame")

def camdb(request, no):
    return StreamingHttpResponse(gen(face_recog.FaceRecog(no), True),content_type="multipart/x-mixed-replace;boundary=frame")

#def check(request, no):    