from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('camera/<int:no>', views.camera, name='camera'),
    path('searchCameraLog/<int:camera_no>', views.searchCameraLog, name='searchCameraLog'),
]