from django.urls import path

from . import views

urlpatterns = [
    path('camdb/<int:no>/', views.camdb, name='camdb'),
    path('cam/<int:no>', views.cam, name='cam'),
    path('cam_register', views.cam_register, name='cam_register'),
]