from django.shortcuts import render
import pytz
import datetime

# Create your views here.

import requests

def trains(request):

    initial_filters = {
        'page[offset]': '0',
        'page[limit]': '50',
        'include': 'trip,schedule',
        'filter[stop]': 'place-north',
        'filter[route_type]': '2',
    }

    response = requests.get('https://api-v3.mbta.com/predictions', params=initial_filters).json()

    trains = []

    for element in response['data']:
        train_info = {}
        train_info['status'] = element['attributes']['status']
        train_info['route'] = element['relationships']['route']['data']['id'][3:]

        time_filters = {
            'include': 'prediction',
            'filter[route]': element['relationships']['route']['data']['id'],
            'filter[direction_id]' : 0
        }

        time_response = requests.get('https://api-v3.mbta.com/schedules', params=time_filters).json()

        train_info['time'] = time_response['data'][0]['attributes']['departure_time'][11:16]
        trains.append(train_info)

    data = {}
    data["context"] = trains


    return render(request, "index_trains.html", data)