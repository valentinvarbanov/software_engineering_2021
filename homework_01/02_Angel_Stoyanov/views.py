from django.http.response import JsonResponse
from django.shortcuts import render

from django.http import HttpResponse

from .models import Currency, CurrencySerializer
from django.db.models import F
import requests

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


def feeling_lucky(request):
    r = requests.get('http://127.0.0.1:8000/crypto/api/v1/lucky')

    context = r.json()

    return render(request, "lucky.html", context)

def feeling_lucky_api(request):
    lucky_choice = Currency.objects.all().annotate(cap=F('price') * F('supply')).order_by('cap-')[0]

    serializer = CurrencySerializer(lucky_choice)

    return JsonResponse(serializer.data)