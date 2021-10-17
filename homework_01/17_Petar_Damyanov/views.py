from django.http.response import JsonResponse
from django.shortcuts import render

from django.http import HttpResponse

from .models import Currency, CurrencySerializer

import random

# Create your views here.

def index(request):
    return render(request, "index.html")

def trending(request):

    trending = Currency.objects.order_by('-price')[0]

    context = {
        "currency_name" : trending.name, 
        "currency_price" : str(trending.price)
    }

    return render(request, "trending.html", context)

def trending_json(request):

    trending = Currency.objects.order_by('-price')[0]

    serializer = CurrencySerializer(trending)

    return JsonResponse(serializer.data)

# 17 % 4 = 1
#Find the bottom 3 currencies with the lowest price and select one by random from those 3.
#This is the lucky one. (This is lucky as it may be as it has the higher growth potential.)
def lucky(request): 
    random_currency = Currency.objects.order_by('price')[random.randint(0, 2)]
    context = {
        "currency_name" : random_currency.name, 
        "currency_price" : str(random_currency.price)
    }

    return render(request, "lucky.html", context)
