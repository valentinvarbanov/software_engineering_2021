from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Currency  # , CurrencySerialiser


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "index.html")


def trending(request):
    trending = Currency.objects.order_by('-price')[0]
    context = {
        "currency_name": trending.name,
        "currency_price": str(trending)
    }
    return render(request, "trending.html", context)


def trending_json(request):
    trending = Currency.objects.order_by('-price')[0]

    serialiser = CurrencySerialiser(trending)

    return JsonResponse(serialiser.data)


def lucky(request):
    highest_price = Currency.objects.order_by('-price')
    print(highest_price)
    highest_supply = highest_price.order_by('-supply')[0]
    print(highest_price.order_by('-supply'))
    context = {
        "currency_name": highest_supply.name,
        "currency_price": str(highest_supply)
    }
    return render(request, "lucky.html", context)
