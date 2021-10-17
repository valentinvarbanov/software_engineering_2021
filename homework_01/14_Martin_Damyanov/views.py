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

def lucky(request):
    cryptoCurrencies = list(Currency.objects.all())
    minCap = cryptoCurrencies[0].price * cryptoCurrencies[0].supply
    resultCurrency = cryptoCurrencies[0]
    for curr in cryptoCurrencies:
        if curr.price * curr.supply < minCap:
            minCap = curr.price * curr.supply
            resultCurrency = curr

    context = {
        "price" : str(resultCurrency.price),
        "supply" : str(resultCurrency.supply),
        "name" : resultCurrency.name,
        "code" : resultCurrency.code,
        "CAP" : str(minCap)
    }
    return render(request, "lucky.html", context)
