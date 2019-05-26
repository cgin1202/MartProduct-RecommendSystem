from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from dashboard.models import Camera
from django.utils import timezone
from myapps import crawlings
from django.views.decorators.csrf import csrf_exempt
import json

#Create your views here.
def backgrounds_index(request):
    template = loader.get_template('backgrounds.html')
    crawling_datas = crawlings.crawlings()
    context = {
        'cameras': Camera.objects.all(),
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def searchBackgrounds_crawlings(request):
    context = []
    now=timezone.localtime()
    now_time = {'time': now.strftime("%H:%M")}
    context.append(now_time)
    crawlings_datas = crawlings.crawlings_db_input()
    return HttpResponse(json.dumps(context), "application/json")