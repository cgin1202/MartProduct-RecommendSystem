from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime, timedelta
from myapps import pymongodb, crawlings
from dashboard.models import CameraLog, Camera, Customer, Product, Realtime
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import json
from django.db.models import Sum


# Create your views here.
def index(request):
    template = loader.get_template('index.html')

    context = {
        'cameras' : Camera.objects.all(),
        'customers' : Customer.objects.all(),
        'products' : Product.objects.all(),
        'no' : 0,
    }
    return HttpResponse(template.render(context, request))

def camera(request, no):
    template = loader.get_template('camera.html')
    context = {
        'cameras' : Camera.objects.all(),
        'products' : Product.objects.all(),
        'no' : no,
    }
    return HttpResponse(template.render(context, request))

def customer(request):
    template = loader.get_template('AllCustomer.html')
    context = {
        'cameras' : Camera.objects.all(),
        'customers' : Customer.objects.all(),
        'products' : Product.objects.all(),    }
    return HttpResponse(template.render(context, request))

def customer_one(request, no):
    template = loader.get_template('Customer.html')
    context = {
        'cameras' : Camera.objects.all(),
        'products' : Product.objects.all(),
        'customer' : Customer.objects.get(customer_no=no),
    }
    return HttpResponse(template.render(context, request))

def ranking(request):
    crawling_datas = crawlings.crawlings()
    template = loader.get_template('ranking.html')
    now=timezone.localtime()
    standard=now-timedelta(days=7)
    # pipeline = [
    #     {"$match" : {"realtime_date" : {"$gte":standard}}},
    #     {"$group": {"_id": "$realtime_product", "realtime_values": {"$sum" : "$realtime_value"}}},
    #     {"$sort":{"realtime_values":-1}},
    # ]
    # mydb = pymongodb.dbconnection()
    # mycol = mydb.dashboard_realtime
    # realtime_db = mycol.aggregate(pipeline)
    # realtimes = []
    # for realtime in realtime_db:
    #     print(realtime)
    #     data = {}
    #     data['realtime_product'] = realtime['_id']
    #     data['realtime_values'] = realtime['realtime_values']
    #     realtimes.append(data)
    realtimes=Realtime.objects.values('realtime_product').filter(realtime_date__gte=standard).annotate(Sum('realtime_value')).order_by('-realtime_value__sum')[:10]

    context = {
        'cameras' : Camera.objects.all(),
        'customers' : Customer.objects.all(),
        'products' : Product.objects.all(),
        'realtimes' : realtimes,
        'crawlings' : crawling_datas
    }
   
    return HttpResponse(template.render(context, request))


@csrf_exempt
def searchCameraLog(request, camera_no):
    now = timezone.localtime()
    earlier = now - timedelta(seconds=1)
    context = []
    cameralogs = CameraLog.objects.filter(datetime_now__gte=earlier)
    
    for cameralog in cameralogs:
        camera_log = {}
        
        camera_log['camera_no'] = cameralog.camera.camera_no
        if(cameralog.camera.product):
            camera_log['product_no'] = cameralog.camera.product.product_no
        if(cameralog.customer):
            customer = cameralog.customer
            camera_log['customer_no'] = customer.customer_no
            camera_log['customer_name'] = customer.customer_name
            camera_log['customer_gender'] = customer.customer_gender
            camera_log['customer_age'] = customer.customer_age
            camera_log['customer_market_in'] = customer.customer_market_in
            

        for k, v in customer.customer_ratings.__dict__.items():
            if k == '_state': continue
            camera_log[str(k)] = int(v)
    
        camera_log['datetime_now'] = str(cameralog.datetime_now)
    # #print(customer.customer_no)
        context.append(camera_log)

    #     context = {'camera_log' : camera_log,'customer_log' : customer_log, 'customer_ratings' : customer_ratings}
    return HttpResponse(json.dumps(context), "application/json")


@csrf_exempt
def searchRatingLog(request, customer_no):
    context = []
    customer = Customer.objects.get(customer_no=customer_no)
    context.append([0, customer.customer_ratings.rating0])
    context.append([1, customer.customer_ratings.rating1])
    context.append([2, customer.customer_ratings.rating2])
    context.append([3, customer.customer_ratings.rating3])
    context.append([4, customer.customer_ratings.rating4])
    context.append([5, customer.customer_ratings.rating5])
    context.append([6, customer.customer_ratings.rating6])
    context.append([7, customer.customer_ratings.rating7])
    context.append([8, customer.customer_ratings.rating8])
    context.append([9, customer.customer_ratings.rating9])
    return HttpResponse(json.dumps(context), "application/json")

