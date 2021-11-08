from django.shortcuts import render

import requests
from django.http.response import JsonResponse
from django.http import HttpResponse
import datetime
# from pytz import timezone


def index(request):

    params = {
        'page[offset]': '0',
        'page[limit]': '10',
        'include': 'schedule,stop,trip',
        'filter[stop]': 'place-north',
        'filter[route_type]': '2', # rail
        'filter[direction_id]': '0',
    }

    response = requests.get('https://api-v3.mbta.com/predictions', params=params).json()
    statuses = {}
    departure_times = {}
    destinations = {}
    trains = {}
    platform_codes = {}
    #print(response)
    lines = []

    for added in response['included']:
        if added['type'] == "stop":
            platform_codes[added['id']] = added['attributes']['platform_code'] #or "TBD"
        if added['type'] == "trip":
            destinations[added['id']] = added['attributes']['headsign']
            trains[added['id']] = added['attributes']['name']
        if added['type'] == "schedule":
            t = added['attributes']['departure_time'][11:19]
            t = datetime.datetime.strptime(t, '%H:%M:%S')
            departure_times[added['id']] = t.strftime("%I:%M %p")
        

    for data in response['data']:
        line = []
        part = data['relationships']
        line.append(departure_times[part['schedule']['data']['id']])
        line.append(destinations[part['trip']['data']['id']])
        line.append(trains[part['trip']['data']['id']])
        if platform_codes[part['stop']['data']['id']] is None:
            line.append("TBD")
        else:
            line.append(platform_codes[part['stop']['data']['id']])
        line.append(data['attributes']['status'])
        # print(line)
        lines.append(line)

    date = datetime.datetime.now()

    context =  {
        'weekday' : date.strftime("%A"),
        'date' : date.strftime("%d-%m-%Y"),
        'time' : date.strftime("%I:%M %p"),
        'lines' : lines
    }
    

    return render(request, "index.html", context)