from django.http.response import JsonResponse
from django.shortcuts import render
import random

from django.http import HttpResponse

from crypto.models import Currency, CurrencySerializer


def index(request):
    return render(request, "index.html")

def trending(request):

    trending = Currency.objects.order_by('-price')[0]
    name = trending.name

    context= {
        'key': str(trending),
        'name': name
    }

    return render(request, "trending.html", context)

    #return HttpResponse("The best trending currency is " + str(trending))

def trending_json(request):
    trending = Currency.objects.order_by('-price')[0]
    
    serializer = CurrencySerializer(trending)

    return JsonResponse(serializer.data)

def lucky(request):

    theChosenOne = random.randint(0,2)
    trending = Currency.objects.order_by('price')[theChosenOne]
    name = trending.name

    context= {
        'key': str(trending),
        'name': name
    }

    return render(request, "lucky.html", context)
