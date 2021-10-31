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
        'filter[stop]':'place-north',
        'filter[route_type]': '2',
    }

    response = requests.get('https://api-v3.mbta.com/predictions', params=initial_filters).json()

    trains, trip_ids = [], []

    for element in response['data']:
        train_info = {}
        train_info['status'] = element['attributes']['status']
        train_info['route'] = element['relationships']['route']['data']['id'][3:]

        #I am lazy person - the numbers on those indices attended both in the route id and the track id
        #That indicated those numbers were connected to something, which after some search appeared to be
        #the train/track/vehicle number. 
        trip_id = element['relationships']['trip']['data']['id']
        trip_ids.append(trip_id)
        train_info['track'] = trip_id[10:14]

        #I hate this part
        for departure in response['included']:
            if departure['type'] == 'schedule':
                for id in trip_ids:
                    if departure['relationships']['trip']['data']['id'] == id:
                        train_info['time'] = departure['attributes']['arrival_time'] or departure['attributes']['departure_time']

        train_info['time'] = train_info['time'][11:16]

        trains.append(train_info)

    data = {}
    data["context"] = trains

    return render(request, "index_trains.html", data)