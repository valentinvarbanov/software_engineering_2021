from django.http.response import JsonResponse
from django.shortcuts import render

from django.http import HttpResponse

from .models import Currency, CurrencySerializer

import requests

# Create your views here.


# https://api.coindesk.com/v1/bpi/currentprice.json

def index(request):

    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response_local = requests.get("https://api.coindesk.com/v1/bpi/currentprice/BGN.json")

    usd = response.json()["bpi"]["USD"]
    bgn = response_local.json()["bpi"]["BGN"]

    context = {
        "bitcoin_price" : usd["rate_float"],
        "bitcoin_price_currency_name" : usd["code"],
        "bitcoin_price_local" : bgn["rate_float"],
        "bitcoin_price_currency_name_local" : bgn["code"]
    }

    return render(request, "index.html", context)

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

