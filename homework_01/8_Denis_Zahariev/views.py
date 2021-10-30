from django.http.response import JsonResponse
from django.shortcuts import render

from django.http import HttpResponse

from .models import Currency, CurrencySerializer

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


def lucky0(request):
    caps = [currency.price * currency.supply for currency in list(Currency.objects.all())]
    lucky = list(Currency.objects.all())[caps.index(max(caps))]

    data = {
        'currencyName': lucky.name,
        'currencyPrice': str(lucky.price),
        'currencyCode': lucky.code,
        'currencySupply': str(lucky.supply)
    }

    return render(request, 'lucky0.html', data)