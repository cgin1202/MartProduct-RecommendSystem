from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime, timedelta
from time import sleep
from myapps import pymongodb, crawlings, face_catching, cf
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
        'customers' : Customer.objects.all().order_by('customer_no')[:10],
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
    template = loader.get_template('customer.html')
    context = {
        'cameras' : Camera.objects.all(),
        'products' : Product.objects.all(),
        'customer' : Customer.objects.get(customer_no=no),
    }
    return HttpResponse(template.render(context, request))

def register(request):
    template = loader.get_template('register.html')
    context = {
        'cameras' : Camera.objects.all(),
    }
    return HttpResponse(template.render(context, request))

def register_picture(request):
    template = loader.get_template('register_picture.html')
    context = {
        'cameras' : Camera.objects.all(),
    }
    return HttpResponse(template.render(context, request))

def billboard(request):
    template = loader.get_template('billboard.html')
    context = {
        'cameras' : Camera.objects.all(),
        'no' : 0,
    }
    return HttpResponse(template.render(context, request))



def ranking(request):
    crawling_datas = crawlings.crawlings()
    template = loader.get_template('ranking.html')
    now=timezone.localtime()
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
    standard=now-timedelta(days=7)
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
def searchRealtimeLog(request):
    context=[]
    now=timezone.localtime()
    standard=now-timedelta(days=7)
    realtimes=Realtime.objects.values('realtime_product').filter(realtime_date__gte=standard).annotate(Sum('realtime_value')).order_by('-realtime_value__sum')
    for realtime in realtimes:
       context.append([realtime['realtime_product'],realtime['realtime_value__sum']])
    return HttpResponse(json.dumps(context), "application/json")


@csrf_exempt
def searchRatingLog(request, customer_no):
    context = []
    log = {}
    customer = Customer.objects.get(customer_no=customer_no)
    customerlog = []
    customerlog.append([0, customer.customer_ratings.rating0])
    customerlog.append([1, customer.customer_ratings.rating1])
    customerlog.append([2, customer.customer_ratings.rating2])
    customerlog.append([3, customer.customer_ratings.rating3])
    customerlog.append([4, customer.customer_ratings.rating4])
    customerlog.append([5, customer.customer_ratings.rating5])
    customerlog.append([6, customer.customer_ratings.rating6])
    customerlog.append([7, customer.customer_ratings.rating7])
    customerlog.append([8, customer.customer_ratings.rating8])
    customerlog.append([9, customer.customer_ratings.rating9])
    log['customerlog'] = customerlog
    now = timezone.localtime()  
    log['timelog'] = str(now)[0:19]
    context.append(log)
    return HttpResponse(json.dumps(context), "application/json")


@csrf_exempt
def face_catch(request):
    context = face_catching.face_catching()
    return HttpResponse(json.dumps(context), "application/json")

@csrf_exempt
def searchRecommendations(request, camera_no):
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

        if customer.customer_no != -1:
            mydb = pymongodb.dbconnection()
            mycol = mydb["dashboard_customer"]
            user_ratings = mycol.find({'customer_no':{'$gte':0}}, {'_id':0, 'customer_no':1, 'customer_ratings':1})
            data_table = {}
            for rating in user_ratings:
                data = {}
                for key, value in rating['customer_ratings'].items():
                    data[int(key[6:])] = value
                data_table[int(rating['customer_no'])] = data
            recommend = cf.getcfratings(data_table, customer.customer_no, 10)
            
            camera_log['ratings'] = [['Product', '순위', '품목 점수', '품목종류', '선호도']]
            recommend_point = []
            for x in recommend['ratings']:
                recommend_point.append(x[1])

            recommend_point = normalization(recommend_point)

            index = 0
            for x in recommend['ratings']:
                product_one = []
                productobj = Product.objects.get(product_no=x[0])
                product_one.append(productobj.product_name)
                product_one.append(index+1)
                product_one.append(int(recommend_point[index]*100))
                product_one.append(str(productobj.product_class))
                product_one.append(int(x[1]))
                camera_log['ratings'].append(product_one)
                index += 1
            

            camera_log['sim_users'] = []
            for sim_users in recommend['sim_users']:
                user = []
                user.append(str(sim_users[0]))
                user.append(sim_users[1])
                camera_log['sim_users'].append(user)
            #camera_log['sim_users'] = recommend['sim_users']
            #camera_log['ratings'] = recommend['ratings']
        else:
            print("done")
            camera_log['sim_users'] = -1
            camera_log['ratings'] = -1
        context.append(camera_log)

    return HttpResponse(json.dumps(context), "application/json")


@csrf_exempt
def showCrawlingdataLog(request):
    context=[]        
    crawling_datas = crawlings.crawlings()
    for naver in crawling_datas['naver']:
        if naver['key'] <= 10:
            context.append([naver['key'],naver['value']])
    for daum in crawling_datas['daum']:
        if daum['key'] <= 10:
            context.append([daum['key'],daum['value']])
    for nate in crawling_datas['nate']:
        if nate['key'] <= 10:
            context.append([nate['key'],nate['value']])    

    now=timezone.localtime()
    context.append([str(now)[0:19]])
    standard=now-timedelta(days=7)
    realtimes=Realtime.objects.values('realtime_product').filter(realtime_date__gte=standard).annotate(Sum('realtime_value')).order_by('-realtime_value__sum')[:10]
    for realtime in realtimes:
        context.append([realtime['realtime_product'],realtime['realtime_value__sum']])
    return HttpResponse(json.dumps(context), "application/json")


def normalization(lists):
    max_val = 0
    min_val = 10000000
    for value in lists:
        if value>max_val:
            max_val = value
        if value < min_val:
            min_val = value
    bottom = max_val - min_val
    result = []
    for value in lists:
        result.append((value-min_val)/bottom)
    return result