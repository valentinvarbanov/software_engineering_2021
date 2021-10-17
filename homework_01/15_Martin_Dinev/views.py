from django.http.response import JsonResponse
from django.shortcuts import render
from crypto.models import Currency

from django.http import HttpResponse
from random import randint

from crypto.models import CurrencySerializer

def index(request):
   # return HttpResponse("<h1>Hello world</h1>")
    return render(request, "index.html")

def trending(request):
    name = Currency.objects.order_by('-price')[0]

    context = {
        'key' : str(name)
    }

    return render(request, "trending.html", context)
    #return HttpResponse("The currently trending currency is " + str(name))

def trending_json(request):
    name = Currency.objects.order_by('-price')[0]

    serializer = CurrencySerializer(name)

    return JsonResponse(serializer.data)

def lucky(request):
    currencies = Currency.objects.order_by('-price')
    rand = randint(0, currencies.count()-1)
    luckyCurrency = currencies[rand]

    context = {
        "currency_name" : luckyCurrency.name,
        "currency_price" : str(luckyCurrency.price),
        "key" : str(luckyCurrency)
    }

    return render(request, "lucky.html", context)