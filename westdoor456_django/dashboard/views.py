from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from myapps import pymongodb
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    mydb = pymongodb.dbconnection()
    pipelines = list()
    pipelines.append({'$sort':{'_id':-1}})
    pipelines.append({'$limit':1})
    camera_log = mydb["camera_log"].aggregate(pipelines)

    context = {
        'no' : 0,
        'camera_log' : camera_log
    }
    return HttpResponse(template.render(context, request))


def camera(request, no):
    return HttpResponse('<html><head><title>Video Streaming Demonstration</title></head><body><h1>Video Streaming Demonstration</h1><img id="bg" src="http://localhost:8000/face_recogg/cam/'+str(no)+'"></body></html>')

@csrf_exempt
def searchCameraLog(request):
    mydb = pymongodb.dbconnection()
    pipelines = list()
    pipelines.append({'$sort':{'_id':-1}})
    pipelines.append({'$limit':1})
    camera_result = mydb["camera_log"].aggregate(pipelines)
    camera_log = {}
    for x in camera_result:
        camera_log['camera_no'] = x['camera_no']
        camera_log['product_no'] = x['product_no']
        camera_log['customer_no'] = x['customer_no']
        camera_log['now_time'] = str(x['now_time'])
        
    context = {'camera_log' : camera_log,}
    return HttpResponse(json.dumps(context), "application/json")