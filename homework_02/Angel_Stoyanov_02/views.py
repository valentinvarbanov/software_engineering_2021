from django.shortcuts import render

import datetime
import requests as requests_api

FETCH_PREDICTIONS_URI = 'https://api-v3.mbta.com/predictions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-departure_time&filter%5Bstop%5D=place-north'
FETCH_VEHICLE_URI = 'https://api-v3.mbta.com/vehicles/'
FETCH_STOP_URI = 'https://api-v3.mbta.com/stops/'


def index(request):
    r = requests_api.get(FETCH_PREDICTIONS_URI)
    data_object = r.json()['data']

    destinations = list()
    statuses = list()

    for _ in data_object:
        try:
            vehicle_id = _['relationships']['vehicle']['data']['id']
            vehicle_attributes = requests_api.get(FETCH_VEHICLE_URI + str(vehicle_id)).json()['data']['attributes']

            statuses.append(vehicle_attributes['current_status'])
        except Exception:
            statuses.append('-')

    for _ in data_object:
        try:
            stop_id = _['relationships']['stop']['data']['id']
            stop_attributes = requests_api.get(FETCH_STOP_URI + str(stop_id)).json()['data']['attributes']

            destinations.append(stop_attributes['name'] + ' - ' + stop_attributes['platform_name'])
        except Exception:
            destinations.append('-')

    __date = datetime.datetime.now()
    _date = __date.strftime('%d %b %Y')
    _time = __date.strftime('%H:%M:%S')

    context = {
        'destinations': destinations,
        'statuses': statuses,
        'main_response': data_object,
        'date': _date,
        'time': _time
    }

    return render(request, 'index.html', context)
