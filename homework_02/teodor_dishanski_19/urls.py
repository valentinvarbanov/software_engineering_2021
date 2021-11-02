from django.urls import path
from . import views

urlpatterns = [
    path('', views.train_board, name='train_board')
]