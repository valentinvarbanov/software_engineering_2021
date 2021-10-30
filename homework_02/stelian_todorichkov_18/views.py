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
        'filter[direction_id]': 0, # only departure
    }

    response = requests.get('https://api-v3.mbta.com/predictions', params=params).json()

    list = []
    
    # get statuses
    for data in response['data']:
        dict = {}
        dict['status'] = data['attributes']['status']
        list.append(dict)
    
    i = 0
    for data in response['included']:
        if i == len(list):
            i = 0
        if data['type'] == 'trip':
            # get train ids
            list[i]['train'] = data['attributes']['name']
            #get destinations
            list[i]['destination'] = data['attributes']['headsign']
        if data['type'] == 'schedule':
            #get departure times
            list[i]['time'] = data['attributes']['departure_time']
        i+=1

    # sort list by time
    for i in range(0, len(list)):
        for k in range(i+1, len(list)):
            
            if list[i]['time'] > list[k]['time']:
                dict = list[i]
                list[i] = list[k]
                list[k] = dict

    # format time 
    for el in list:
        el['time'] = datetime.fromisoformat(el['time']).astimezone(timezone('America/New_York')).strftime('%I:%M %p')
               

       



    cur_time = datetime.now().astimezone(timezone('America/New_York')).strftime('%I:%M:%S %p')

    context = {
        'data': list,
        'time': cur_time
    }

    return render(request, "board.html", context)


