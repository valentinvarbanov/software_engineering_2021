from django.shortcuts import render

import requests
from django.http.response import JsonResponse
from django.http import HttpResponse




def index(request):
    response = requests.get("https://api-v3.mbta.com/predictions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-departure_time&filter%5Bstop%5D=place-north")
    # print(response.json())
    context = {
        "some" : "text"
    }
    if(response.status_code == 200):
        print("Ok")
        context = {
            "data" : response.json()['data']
        }
    
    return render(request, 'index.html', context)
    #return JsonResponse(context)
    #return HttpResponse("Hi")
        


# Create your views here.
 # 