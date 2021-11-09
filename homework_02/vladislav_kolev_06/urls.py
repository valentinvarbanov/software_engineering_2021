from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='train_station_board')
]
