import random
from django.http.response import JsonResponse
from django.shortcuts import render

from django.http import HttpResponse

from .models import Currency, CurrencySerializer

from random import randint

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

def lucky(request):

    lucky_index = randint(0, 2)

    lucky = Currency.objects.order_by('-price')[lucky_index]

    context = {
        "currency_name" : lucky.name, 
        "currency_price" : str(lucky.price)
    }
    return render(request, 'lucky.html', context)