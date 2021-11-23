from django.http import response
from django.http.response import JsonResponse
from django.shortcuts import render

from django.http import HttpResponse
import requests
import datetime


def dashboard(request):
    
    response = requests.get('https://api-v3.mbta.com/predictions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-departure_time&filter%5Bstop%5D=place-north')
    response_json = response.json()
    mapped_data = response_json['data']

    current_time = datetime.datetime.now()

    today_date = current_time.strftime("%d.%m.%Y")
    curr_time = current_time.strftime("%H:%M:%S")

    routes = []

    for i in mapped_data:
        try:
            route_vehicle = requests.get("https://api-v3.mbta.com/stops/" + i["relationships"]["stop"]["data"]["id"])
            route_json = route_vehicle.json()["data"]["attributes"]["platform_name"]
            routes.append(route_json)
        except:
            routes.append("No route")

    statuses = []

    for i in mapped_data:
        try:
            status_vehicle = requests.get("https://api-v3.mbta.com/vehicles/" + i["relationships"]["vehicle"]["data"]["id"])
            status_json = status_vehicle.json()["data"]["attributes"]["current_status"]
            statuses.append(status_json)
        except:
            statuses.append("No status")

    context = {
        'data': response_json['data'],
        'date': today_date,
        'time': curr_time,
        'routes': routes,
        'statuses': statuses
    }
    
    return render(request, "dashboard.html", context)