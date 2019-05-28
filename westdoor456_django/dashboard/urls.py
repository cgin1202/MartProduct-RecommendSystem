from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('camera/<int:no>', views.camera, name='camera'),
    path('customer', views.customer, name='customer'),
    path('customer/<int:no>', views.customer_one, name='customer_one'),
    path('searchRealtimeLog', views.searchRealtimeLog, name='searchRealtimeLog'),
    path('searchCameraLog/<int:camera_no>', views.searchCameraLog, name='searchCameraLog'),
    path('searchRatingLog/<int:customer_no>', views.searchRatingLog, name='searchRatingLog'),
    path('searchRecommendations/<int:camera_no>', views.searchRecommendations, name='searchRecommendations'),
    path('billboard', views.billboard, name='billboard'),
    path('register', views.register, name='register'),
    path('register_picture', views.register_picture, name='register_picutre'),
    path('ranking', views.ranking, name='ranking'),
    path('face_catch', views.face_catch, name='face_catch'),
    path('showCrawlingdataLog', views.showCrawlingdataLog, name='showCrawlingdataLog'),
]