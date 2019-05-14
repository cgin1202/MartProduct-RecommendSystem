from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime, timedelta
from myapps import pymongodb
from dashboard.models import CameraLog
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import json

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    mydb = pymongodb.dbconnection()

    context = {
        'no' : 0,
    }
    return HttpResponse(template.render(context, request))

def camera(request, no):
    return HttpResponse('<html><head><title>Video Streaming Demonstration</title></head><body><h1>Video Streaming Demonstration</h1><img id="bg" src="http://localhost:8000/face_recogg/cam/'+str(no)+'"></body></html>')

@csrf_exempt
def searchCameraLog(request):
    now = timezone.localtime()
    earlier = now - timedelta(seconds=1)
    context = []
    cameralogs = CameraLog.objects.filter(datetime_now__gte=earlier)
    
    for cameralog in cameralogs:
        camera_log = {}
        customer_log = {}
        rating_log = {}
        
        camera_log['camera_no'] = cameralog.camera_no.camera_no
        camera_log['product_no'] = cameralog.camera_no.product_no
        customer = cameralog.customer_no
        customer_log['customer_no'] = customer.customer_no
        customer_log['customer_name'] = customer.customer_name
        customer_log['customer_gender'] = customer.customer_gender
        customer_log['customer_age'] = customer.customer_age
        customer_log['customer_market_in'] = customer.customer_market_in
        

        for k, v in customer.customer_ratings.__dict__.items():
            if k == '_state': continue
            rating_log[str(k)] = int(v)
    
    #     camera_log['datetime_now'] = str(cameralog.datetime_now)
    # #print(customer.customer_no)
        context.append((camera_log, customer_log, rating_log))

    #     context = {'camera_log' : camera_log,'customer_log' : customer_log, 'customer_ratings' : customer_ratings}
    return HttpResponse(json.dumps(context), "application/json")