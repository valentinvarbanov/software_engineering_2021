from django.urls import path
from . import views

urlpatterns = [
    path('', views.train_data, name='train_station_board')
]
