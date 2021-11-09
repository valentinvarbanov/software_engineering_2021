from django.shortcuts import render
from django.http import response
from django.http.response import JsonResponse
from django.http import HttpResponse
from requests.models import ContentDecodingError
import requests, json
import datetime
import itertools
import pytz
def index(request): 

    params = {
        "sort" : "-arrival_time",
        "filter[direction_id]" : "0",
        "page[offset]" : "0",
        "include" : "trip,schedule",
        "page[limit]" : "100",
        "filter[route_type]" : "2",
        "filter[stop]" : "place-north",
        "filter[direction_id]" : "0",
    }

    now = datetime.datetime.now(pytz.timezone('America/New_York'))
    response = requests.get('https://api-v3.mbta.com/predictions', params=params).json()

    table_content = []
    
    for data in response['data']:
        record = dict()
        record['status'] = data['attributes']['status']
        rel = data['relationships']
        record['tripID'] = rel['trip']['data']['id']
        record['stopID'] = rel['stop']['data']['id']
        table_content.append(record)
    
    for data in response['included']:
        for row in table_content:
            if data['type'] == 'trip':
                if row['tripID'] == data['id']:
                    row['destination'] = data['attributes']['headsign']
                    row['train'] = data['attributes']['name']
                    break
            elif data['type'] == 'schedule':
                if row['tripID'] in data['id']:
                    dest_time = datetime.datetime.fromisoformat(str(data['attributes']['departure_time'])).strftime("%I:%M %p").upper()
                    row['time'] = dest_time
                    break
            elif data['type'] == 'stop':
                if row['stopID'] == data['id']:
                    if data['attributes']['platform_code'] is None or len(data['attributes']['platform_code'])<1:
                        row['track'] = 'TBD'
                    else: 
                        row['track'] = data['attributes']['platform_code']

    table_content = sorted(table_content, key = lambda i: i['time'])

    context = {
        'data': table_content,
        'time_day': now.strftime("%A"),
        'now_time': now.strftime("%m - %d - %Y"),
    }

    return render(request, "index.html", context = context)