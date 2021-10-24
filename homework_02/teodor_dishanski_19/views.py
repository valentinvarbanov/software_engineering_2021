from django.shortcuts import render

from django.http import HttpResponse, response
from django.http.response import JsonResponse

from requests.models import ContentDecodingError

import requests
import datetime
import json, pytz

# Create your views here.

def train_board(request):
    #   To present the train station departure board, we should find the time in Massachusetts.
    current_time = datetime.datetime.now(pytz.timezone('America/New_York'))

    #   We get the predictions API and convert them into a JSON object.
    response = requests.get("https://api-v3.mbta.com/predictions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-departure_time&filter%5Bstop%5D=place-north")
    response_json_format = response.json()

    #   We will need 2 lists - 1 to store the routes and 1 to store the statuses of the vehicles.
    routes_vehicles, statuses_vehicles = [], []

    #  Firstly, we make a loop through the response data to get the information about the routes of the vehicles.
    #   We get the id of the stops from the relationships of every single prediction.
    #   If we do not have any data for it, we store that there is no route.
    for i in response_json_format['data']:
        try:
            route_vehicle = requests.get("https://api-v3.mbta.com/stops/" + i["relationships"]["stop"]["data"]["id"])
            route_json_format = route_vehicle.json()["data"]["attributes"]["description"]
            routes_vehicles.append(route_json_format)
        except:
            routes_vehicles.append("No route")

    #  Secondly, we make a loop through the response data to get the information about the statuses of the vehicles.
    #   We get the id of the vehicles from the relationships of every single prediction.
    #   If we do not have any data for it, we store that there is no status.
    for i in response_json_format['data']:
        try:
            status_vehicle = requests.get("https://api-v3.mbta.com/vehicles/" + i["relationships"]["vehicle"]["data"]["id"])
            status_json_format = status_vehicle.json()["data"]["attributes"]["current_status"]
            statuses_vehicles.append(status_json_format)
        except:
            statuses_vehicles.append("No status")

    context = {
        'day': current_time.strftime("%A"),
        'date': current_time.strftime("%m - %d - %Y"),
        'time': current_time.strftime("%H:%M"),

        'data': response_json_format,
        'routes': routes_vehicles,
        'statuses': statuses_vehicles
    }

    return render(request, "train_board.html", context)

