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

    trains = []

    for element in response['data']:
        train_info = {}
        train_info['status'] = element['attributes']['status']
        train_info['route'] = element['relationships']['route']['data']['id'][3:]

        #I am lazy person - the numbers on those indices attended both in the route id and the track id
        #That indicated those numbers were connected to something, which after some search appeared to be
        #the train/track/vehicle number.  
        train_info['track'] = element['relationships']['trip']['data']['id'][10:14]
       

        #Instead of searching in the monstrosity of lists and dicts in the response I preferred to
        #send request with filters. The filters will significantly reduce the number of schedules, and thus,
        #the amount of data, that is sent back to the django server.
        time_filters = {
            'include': 'prediction',
            'filter[trip]': element['relationships']['trip']['data']['id'],
            'filter[stop]':'place-north',
            'filter[route_type]': '2'
        }

        time_response = requests.get('https://api-v3.mbta.com/schedules', params=time_filters).json()

        train_info['time'] = time_response['data'][0]['attributes']['arrival_time'] or time_response['data'][0]['attributes']['departure_time']
        train_info['time'] = train_info['time'][11:16]

        trains.append(train_info)

    data = {}
    data["context"] = trains


    return render(request, "index_trains.html", data)