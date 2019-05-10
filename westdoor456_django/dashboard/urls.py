from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('camera/<int:no>', views.camera, name='camera'),
    path('searchCameraLog/', views.searchCameraLog, name='searchCameraLog'),
]