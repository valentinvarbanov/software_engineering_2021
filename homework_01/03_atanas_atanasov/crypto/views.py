from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse

from .forms import CoinForm
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

def addCoin(request):
    form = CoinForm
    if request.method == 'POST':
        form = CoinForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form':form}
    return render(request, "addCoin.html", context)

def lucky(request):
    coins = Currency.objects.order_by('-price')[:3]
    lucky_coin = random.choice(coins)

    context = {'lucky_coin':lucky_coin}
    random.seed()
    return render(request, "lucky.html", context)