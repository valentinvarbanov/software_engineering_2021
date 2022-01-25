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

def lucky_func(request):
    lucky_cur = sorted(list(Currency.objects.all()), key=lambda cur: cur.price * cur.supply)[0]

    context = {
        'cur_name' : lucky_cur.name,
        'cur_price' : str(lucky_cur.price),
        'cur_code' : lucky_cur.code,
        'cur_supply' : str(lucky_cur.supply)
    }
    
    return render(request, 'luck.html', context)



