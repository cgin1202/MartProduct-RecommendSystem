from django.urls import path

from . import views

urlpatterns = [
    path('camdb/<int:no>/', views.camdb, name='camdb'),
    path('cam/<int:no>', views.cam, name='cam'),
]