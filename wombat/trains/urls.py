from django.urls import path

from . import views

urlpatterns = [
    path('', views.trains, name='trains'),
]