from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('trending', views.trending, name='trending'),
    path('lucky_0', views.lucky_0, name='lucky_page_0'),
    path('lucky_1', views.lucky_1, name='lucky_page_1'),
    path('lucky_2', views.lucky_2, name='lucky_page_2'),
    path('lucky', views.lucky_3, name='lucky_page_3'),
    path('api/v1/trending', views.trending_json, name="trending_api"),
]