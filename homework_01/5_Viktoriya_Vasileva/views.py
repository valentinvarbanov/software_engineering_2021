#from django.db.models.expressions import Random
from django.shortcuts import render

from django.http import HttpResponse

from .models import Currency
import random

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def trending(request):
    trending = Currency.objects.order_by('-price')[0]

    return HttpResponse("The currently trending currency is " + 
    trending.name + " " + str(trending))

def lucky(request):
    mod = 5%4
    losers = [Currency.objects.order_by('price')[0], Currency.objects.order_by('price')[1], Currency.objects.order_by('price')[2]]
    chosen_one = losers[random.randint(0, 2)]
    content = {
        "currency_name" : chosen_one.name,
        "currency_price" : chosen_one.price,
        "currency_code" :chosen_one.code
    }
    
    return render(request, "lucky.html", content)
    #Sreturn HttpResponse("Contragulations!")
