from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('camera/<int:no>', views.camera, name='camera'),
    path('customer', views.customer, name='customer'),
    path('customer/<int:no>', views.customer_one, name='customer_one'),
    path('searchCameraLog/<int:camera_no>', views.searchCameraLog, name='searchCameraLog'),
    path('searchRatingLog/<int:customer_no>', views.searchRatingLog, name='searchRatingLog'),
    path('ranking', views.ranking, name='ranking'),
]