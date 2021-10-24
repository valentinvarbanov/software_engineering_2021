from django.http import HttpResponse, response
from django.http.response import JsonResponse
from django.shortcuts import render

from requests.models import ContentDecodingError

import requests
from datetime import datetime
import json

def board(request):
    response = requests.get('https://api-v3.mbta.com/predictions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-departure_time&filter%5Bstop%5D=place-north')

    response_json = response.json()

    routes = []
    vehicle_status = []

    for i in response_json['data']:
        try:
            stop_id = request.get('https://api-v3.mbta.com/stops/' + i['relationships']['stop']['data']['id'])
            route = stop_id.json()['data']['attributes']['description']
            routes.append(route)
        except:
            routes.append("No route")

    for i in response_json['data']:
        try:
            vehicle_id = requests.get('https://api-v3.mbta.com/vhicles/' + i['relationships']['vehicles']['data']['id'])
            status = vehicle_id.json()['data']['attributes']['current_srtatus']
            vehicle_status.append(status)
        except:
            vehicle_status.append('No status')


    cur_time = datetime.now()

    context = {
        'day' : cur_time.strftime("%A"),
        'date' : cur_time.strftime("%D-%M-%Y"),
        'time' : cur_time.strftime("%H:%M"),

        'data' : response_json,
        'routes' : routes,
        'statuses' : vehicle_status,
    }

    return render(request, "board.html", context)


