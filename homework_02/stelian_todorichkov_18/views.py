from django.shortcuts import render

import requests
from datetime import datetime
from pytz import timezone

def board(request):

    params = {
        'page[offset]': '0',
        'page[limit]': '10',
        'include': 'trip,schedule',
        'filter[stop]': 'place-north',
        'filter[route_type]': '2', # rail
        'filter[direction_id]': '0', # only departure
    }

    response = requests.get('https://api-v3.mbta.com/predictions', params=params).json()

    list = []
    
    # get statuses
    for data in response['data']:
        dict = {}
        dict['status'] = data['attributes']['status']
        dict['id'] = data['relationships']['trip']['data']['id']
        list.append(dict)
    
    for data in response['included']:
        for el in list:
            if data['type'] == 'trip' and el['id'] == data['id']:
                # get train ids
                el['train'] = data['attributes']['name']
                #get destinations
                el['destination'] = data['attributes']['headsign']
            if data['type'] == 'schedule' and el['id'] in data['id']:
                #get departure times
                el['time'] = data['attributes']['departure_time']

    # sort list by time
    list = sorted(list, key = lambda i: i['time'])
    
    # format time 
    for el in list:
        el['time'] = datetime.fromisoformat(el['time']).strftime('%I:%M %p')
        
    cur_time = datetime.now().astimezone(timezone('America/New_York')).strftime('%I:%M:%S %p')

    context = {
        'data': list,
        'time': cur_time,
    }

    return render(request, "board.html", context)


