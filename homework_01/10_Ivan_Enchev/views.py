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
        "currency_name": trending.name,
        "currency_price": str(trending.price)
    }

    return render(request, "trending.html", context)


def trending_json(request):
    trending = Currency.objects.order_by('-price')[0]

    serializer = CurrencySerializer(trending)

    return JsonResponse(serializer.data)


def lucky(request):
    all_currencies = Currency.objects.all()

    best_currency = all_currencies[0]
    for i in all_currencies:
        if (i.price * i.supply) < (best_currency.price * best_currency.supply):
            best_currency = i

    context = {
        'currency_name': best_currency.name
    }
    render(request, lucky.html, context)
