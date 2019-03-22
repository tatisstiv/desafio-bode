from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path(r'^(?P<pk>\d+)$', views.rent, name='rent'),
]
