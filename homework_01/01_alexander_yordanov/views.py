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

def lucky_one(request):
    random_crypto =  random.choice(Currency.objects.order_by('price')[:3])

    context = {
        "currency_name" : random_crypto.name,
        "currency_price" : random_crypto.price,
        "currency_code" : random_crypto.code,
        "currency_supply" : random_crypto.supply
    }
    
    return render(request, "luck.html", context)