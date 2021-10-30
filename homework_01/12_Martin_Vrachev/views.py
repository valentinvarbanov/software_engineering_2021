from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

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
    # I am number 12, therefore the base value is 12 % 4 = 0
    
    base_value = 0

    lucky_coin = Currency.objects.all()
    max = lucky_coin[0]
    for i in lucky_coin:
        if(i.price * i.supply > max.price * max.supply):
            max = i


    context = {
        'c_name': max.name,
        'c_price': max.price,
        'c_supply': max.supply
    }


    return render(request, 'lucky.html', context)


