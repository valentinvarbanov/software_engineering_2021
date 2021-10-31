from django.shortcuts import render
import datetime
from pytz import timezone
import requests

# Create your views here.

def departure_board(request):

    now = datetime.datetime.now(timezone('US/Eastern'))
    weekday = now.strftime('%A')
    date = now.strftime('%m-%d-%Y')
    time = now.strftime('%l:%M %p')

    params = {
    'page[offset]': '0',
    'page[limit]': '10',
    'sort': 'departure_time',
    'include': 'trip,stop',
    'filter[stop]': 'place-north',
    'filter[route_type]': '2'
    }

    response = requests.get('https://api-v3.mbta.com/predictions', params=params).json()

    destinations = []
    track_no = []
    train_no = []

    for req in response['data']:
        dest = requests.get('https://api-v3.mbta.com/trips/' + req['relationships']['trip']['data']['id'])
        destinations.append(dest.json()['data']['attributes']['headsign'])
        train_no.append(dest.json()['data']['attributes']['name'])

# I get KeyError for some reason
#    for req in response['data']:
#       track = requests.get('https://api-v3.mbta.com/stops/' + req['relationships']['stop']['data']['id'])
#        track_no.append(track.json()['data']['attributes']['platform_code'])


    context = {
        'weekday': weekday,
        'date': date,
        'time': time,
        'response': response['data'],
        'destinations': destinations,
        'train_no': train_no,
        'track_no': track_no
    }

    return render(request, "departure_board.html", context)


   # params = {'page[offset]': '0', 'page[limit]': '10', 'sort': 'departure_time', 'include': 'trip,schedule,stop', 'filter[stop]': 'place-north', 'filter[route_type]': '2'}
