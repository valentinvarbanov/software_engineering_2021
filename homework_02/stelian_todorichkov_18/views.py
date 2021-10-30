from django.shortcuts import render

import requests
from datetime import datetime
from pytz import timezone

def board(request):
    
    #param for requst
    params = {
        'page[offset]': '0',
        'page[limit]': '10',
        'include': 'trip,schedule,stop',
        'filter[stop]': 'place-north',
        'filter[route_type]': '2', # rail
        'filter[direction_id]': '0', # only departure
    }

    #make get request to get json data from API
    response = requests.get('https://api-v3.mbta.com/predictions', params=params).json()

    # list for all arguments (time, destination, train#, track#, status)
    list = []
    
    # get statuses, trip and stop ids
    for data in response['data']:
        dict = {}
        dict['status'] = data['attributes']['status']
        dict['trip_id'] = data['relationships']['trip']['data']['id']
        dict['stop_id'] = data['relationships']['stop']['data']['id']
        list.append(dict)
    
    for data in response['included']:
        for el in list:
            if data['type'] == 'trip' and el['trip_id'] == data['id']:
                # get train ids
                el['train'] = data['attributes']['name']
                #get destinations
                el['destination'] = data['attributes']['headsign']
                break
            if data['type'] == 'schedule' and el['trip_id'] in data['id']:
                #get departure times
                el['time'] = data['attributes']['departure_time']
                break
            if data['type'] == 'stop' and el['stop_id'] == data['id']:
                #get track
                if data['attributes']['platform_code'] is None:
                   el['track'] = 'TBD'
                else: 
                    el['track'] = data['attributes']['platform_code']

    # sort list by time
    list = sorted(list, key = lambda i: i['time'])

    # format time 
    for el in list:
        el['time'] = datetime.fromisoformat(el['time']).strftime('%I:%M %p')

    # get curr time with timezone New Yourk   
    cur_time = datetime.now().astimezone(timezone('America/New_York')).strftime('%I:%M:%S %p')

    # data for send to HTML
    context = {
        'data': list,
        'time': cur_time,
    }

    return render(request, "board.html", context)