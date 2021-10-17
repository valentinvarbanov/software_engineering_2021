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

# with 2 base value 
def lucky(request): 
    all_currencies = list(Currency.objects.all())
    all_currencies_caps = [currency.price * currency.supply for currency in all_currencies]
    
    currenct_with_min_cap = all_currencies[all_currencies_caps.index(min(all_currencies_caps))]


    context = {
        "currency_name" : currenct_with_min_cap.name, 
        "currency_price" : str(currenct_with_min_cap.price),
        "currency_code" : currenct_with_min_cap.code,
        "currency_supply" : str(currenct_with_min_cap.supply)
    }


    return render(request, "lucky.html", context)