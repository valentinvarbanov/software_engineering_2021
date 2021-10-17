from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('trending', views.trending, name='trending'),
    path('lucky', views.feeling_lucky, name='feeling_lucky'),
    path('api/v1/trending', views.trending_json, name="trending_api"),
    path('api/v1/lucky', views.feeling_lucky_api, name="feeling_lucky_api"),
]