from django.shortcuts import render

from django.http import HttpResponse

from .models import Currency

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the crypto index.")

def trending(request):

    trending = Currency.objects.order_by('-price')[0]

    return HttpResponse("The currently trending currency is " + trending.name + " " + str(trending))
