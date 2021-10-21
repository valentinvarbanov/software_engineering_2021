from django.http import response
from django.shortcuts import render
from django.http.response import JsonResponse
from django.http import HttpResponse
from requests.models import ContentDecodingError
import requests, json
import datetime
import itertools

def index(request): 
    now = datetime.datetime.now()
    response = requests.get("https://api-v3.mbta.com/predictions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-departure_time&filter%5Bstop%5D=place-north", headers={"X-API-Key":"537204397425447493511cec18bfc0fa"})
    names = []
    statuses = []
    data = response.json()

    for i in data['data']:
        try:
            name = requests.get("https://api-v3.mbta.com/stops/" + i["relationships"]["stop"]["data"]["id"]).json()["data"]["attributes"]["description"]
            names.append(name)
        except:
            names.append("No route")

    for i in data['data']:
        try:
            status = requests.get("https://api-v3.mbta.com/vehicles/" + i["relationships"]["vehicle"]["data"]["id"]).json()["data"]["attributes"]["current_status"]
            statuses.append(status)

        except:
            statuses.append("No status")


    content = {
        'data': response.json(),
        'time_day': now.strftime("%A"),
        'now_time': now.strftime("%m - %d - %Y"),
        'names': names,
        'statuses': statuses
    }

    return render(request, "api.html", context = content)
