from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('trending', views.trending, name='trending'),
    path('api/v1/trending', views.trending_json, name="trending_api"),
    path('lucky', views.lucky, name="lucky")
]