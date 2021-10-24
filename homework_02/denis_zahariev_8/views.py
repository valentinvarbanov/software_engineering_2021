from django.shortcuts import render
from django.http import response
from django.http.response import JsonResponse
from django.http import HttpResponse
from requests.models import ContentDecodingError
import requests, json
import datetime
import itertools
import pytz
def index(request): 
    now = datetime.datetime.now(pytz.timezone('America/New_York'))
    response = requests.get("https://api-v3.mbta.com/predictions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-departure_time&filter%5Bstop%5D=place-north", headers={"X-API-Key":"537204397425447493511cec18bfc0fa"})
    vehicle_routes, vehicle_status = list(), list()
    data = response.json()

    for i in data['data']:
        try:
            route = requests.get("https://api-v3.mbta.com/stops/" + i["relationships"]["stop"]["data"]["id"]).json()["data"]["attributes"]["description"]
            vehicle_routes.append(route)
        except:
            vehicle_routes.append("No route")

        try:
            status = requests.get("https://api-v3.mbta.com/vehicles/" + i["relationships"]["vehicle"]["data"]["id"]).json()["data"]["attributes"]["current_status"]
            vehicle_status.append(status)
        except:
            vehicle_status.append("No status")


    table_content = list()

    for i, val in enumerate(data['data']):
        table_content.append([
                            val['attributes']['arrival_time'].replace("T",'\n') if val['attributes']['arrival_time'] != None else None, 
                            val['attributes']['departure_time'].replace("T",'\n') if val['attributes']['departure_time'] != None else None, 
                            val['relationships']['vehicle']['data']['id'],
                            vehicle_routes[i],
                            vehicle_status[i]])

    context = {
        'data': table_content,
        'time_day': now.strftime("%A"),
        'now_time': now.strftime("%m - %d - %Y"),
    }

    return render(request, "index.html", context = context)