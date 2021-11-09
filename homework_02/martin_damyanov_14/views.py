from django.shortcuts import render
import requests
from datetime import datetime
from pytz import timezone
import calendar


def api(request):
    params = {
        'page[offset]': '0',
        'page[limit]': '10',
        'include': 'trip,schedule,stop',
        'filter[stop]': 'place-north',
        'filter[route_type]': '2', # rail
        'filter[direction_id]': '0', # only departure
    }

    response = requests.get('https://api-v3.mbta.com/predictions', params=params).json()
    
    infoArr = []

    for data in response['data']:
        dict = {}
        dict['status'] = data['attributes']['status']
        dict['trip_id'] = data['relationships']['trip']['data']['id']
        dict['stop_id'] = data['relationships']['stop']['data']['id']
        infoArr.append(dict)

    for data in response['included']:
        for el in infoArr:
            if data['type'] == 'trip' and el['trip_id'] == data['id']:
                # get train ids
                el['train'] = data['attributes']['name']
                #get destinations
                el['destination'] = data['attributes']['headsign']
                break
            if data['type'] == 'schedule' and el['trip_id'] in data['id']:
                #get departure times
                el['time'] = datetime.fromisoformat(data['attributes']['departure_time']).strftime('%I:%M %p')
                #el['time'] = datetime.fromisoformat(el['time']).strftime('%I:%M %p')
                break
            if data['type'] == 'stop' and el['stop_id'] == data['id']:
                if data['attributes']['platform_code'] is None:
                   el['track'] = 'TBD'
                else: 
                    el['track'] = data['attributes']['platform_code']

            

    

    infoArr = sorted(infoArr, key = lambda train: train['time'])
    cur_time = datetime.now(timezone('America/New_York'))
    context = {
        "cur_year" : cur_time.year,
        "cur_date" : cur_time.day,
        "cur_month" : cur_time.month,
        "cur_weekday" : calendar.day_name[cur_time.weekday()],
        "cur_time" : cur_time.strftime("%H:%M:%S"),
        'data': infoArr,
    }

    return render(request, "timetable.html", context)