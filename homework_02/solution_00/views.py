from django.shortcuts import render

import requests
from requests.sessions import PreparedRequest

import datetime
import pytz

# Create your views here.

def index(request):

    params = {
        "page[offset]" : "0",
        "page[limit]" : "50",
        "sort" : "-departure_time",
        "include" : "stop,schedule,trip",
        "filter[direction_id]" : "0", # departing
        "filter[route_type]" : "2", # rail only
        "filter[stop]" : "place-north",
    }

    predictions_response = requests.get('https://api-v3.mbta.com/predictions', params=params)

    json = predictions_response.json()

    predictions = []
    schedules = {}
    stops = {}
    trips = {}

    for element in json['data']:

        if element['type'] == 'prediction':
            predictions.append(element)

    for element in json['included']:
        if element['type'] == 'schedule':
            schedules[element['id']] = element
        
        if element['type'] == 'stop':
            stops[element['id']] = element
        
        if element['type'] == 'trip':
            trips[element['id']] = element

    # print("predictions: " + str(len(predictions)))
    # print("schedules: " + str(len(schedules)))
    # print("stops: " + str(len(stops)))
    # print("trips: " + str(len(trips)))

    display_items = []

    for prediction in predictions:

        display_item = {}

        # status
        display_item['status'] = prediction['attributes']['status']

        # destination & train number
        trip_id = prediction['relationships']['trip']['data']['id']
        trip = trips[trip_id]['attributes']

        display_item['destination'] = trip['headsign']
        display_item['train'] = trip['name']

        # leaving time
        schedule_id = prediction['relationships']['schedule']['data']['id']
        schedule = schedules[schedule_id]['attributes']

        departure = datetime.datetime.fromisoformat(schedule['departure_time'])
        display_item['time'] = departure.strftime('%H:%M %p')

        # platform
        stop_id = prediction['relationships']['stop']['data']['id']
        stop = stops[stop_id]['attributes'] 
        
        display_item['track'] = stop['platform_code'] or "TBD" # null -> TBD

        display_items.append(display_item)

    # sort
    display_items.sort(key=lambda p: p['time'])

    now = datetime.datetime.now(pytz.timezone('America/New_York'))
    
    context = {
        'display_items': display_items,
        'current_time': now.strftime('%H:%M:%S %p')
    }

    return render(request, 'solution.html', context)