from django.urls import path

from . import views

urlpatterns = [
    path('cam/<int:no>', views.cam, name='cam'),
]