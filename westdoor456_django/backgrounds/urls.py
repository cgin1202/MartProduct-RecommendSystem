from django.urls import path
from . import views

urlpatterns = [
    path('', views.backgrounds_index, name='backgrounds_index'),
    path('searchBackgrounds_crawlings', views.searchBackgrounds_crawlings, name='searchBackgrounds_crawlings'),
]
#views.hello(repeat=10, repeat_until=None)
