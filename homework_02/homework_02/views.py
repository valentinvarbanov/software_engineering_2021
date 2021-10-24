from django.shortcuts import render
from urllib.request import Request

from . import templates

import requests
import datetime

#import requests

def timetable(request):
    response = requests.get("https://api-v3.mbta.com/predictions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-departure_time&filter%5Bstop%5D=place-north")
    raw_data = response.json()
    routes = []
    statuses = []

    for i in raw_data['data']:
        try:
            route = requests.get("https://api-v3.mbta.com/stops/" + i["relationships"]["stop"]["data"]["id"]).json()["data"]["attributes"]["description"]
            routes.append(route)
        except:
            routes.append("No route")

    for i in raw_data['data']:
        try:
            status = requests.get("https://api-v3.mbta.com/vehicles/" + i["relationships"]["vehicle"]["data"]["id"]).json()["data"]["attributes"]["current_status"]
            statuses.append(status)

        except:
            statuses.append("No status")

    now = datetime.datetime.now()
    context = {
        'data': raw_data,
        'routes': routes,
        'statuses': statuses,
        'day': now.strftime("%A"),
        'date': now.strftime("%m - %d - %Y")
    }

    return render(request, "timetable.html", context=context)