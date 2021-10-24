from django.urls import path
from . import views

urlpatterns = [
    path('', views.departure_board(), name="departure_board")
]