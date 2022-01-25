from django.http.response import JsonResponse
from django.shortcuts import render

from django.http import HttpResponse

from .models import Currency, CurrencySerializer

import random   # Used for choosing random element in a list

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


def lucky_0(request) -> HttpResponse:
    caps = [currency.price * currency.supply for currency in list(Currency.objects.all())]
    lucky_currency = list(Currency.objects.all())[caps.index(max(caps))]

    context = {
        'currency_name': lucky_currency.name,
        'currency_price': str(lucky_currency.price),
        'currency_code': lucky_currency.code,
        'currency_supply': str(lucky_currency.supply)
    }

    return render(request, 'lucky_0.html', context)


def lucky_1(request) -> HttpResponse:
    lucky_currency = random.choice(Currency.objects.order_by('price')[:3])

    context = {
        'currency_name': lucky_currency.name,
        'currency_price': str(lucky_currency.price),
        'currency_code': lucky_currency.code,
        'currency_supply': str(lucky_currency.supply)
    }

    return render(request, 'lucky_1.html', context)


def lucky_2(request) -> HttpResponse:
    caps = [currency.price * currency.supply for currency in list(Currency.objects.all())]
    lucky_currency = list(Currency.objects.all())[caps.index(min(caps))]


    context = {
        'currency_name': lucky_currency.name,
        'currency_price': str(lucky_currency.price),
        'currency_code': lucky_currency.code,
        'currency_supply': str(lucky_currency.supply)
    }

    return render(request, 'lucky_2.html', context)


def lucky_3(request) -> HttpResponse:
    lucky_currency = random.choice(Currency.objects.order_by('-price')[:3])

    context = {
        'currency_name': lucky_currency.name,
        'currency_price': str(lucky_currency.price),
        'currency_code': lucky_currency.code,
        'currency_supply': str(lucky_currency.supply)
    }

    return render(request, "lucky.html", context)
