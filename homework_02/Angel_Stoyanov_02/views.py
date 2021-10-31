import datetime
import pytz

import requests as requests_api
from django.shortcuts import render

FETCH_PREDICTIONS_URI = 'https://api-v3.mbta.com/predictions'

params = {
    'page[offset]': '0',
    'page[limit]': '10',
    'sort': 'departure_time',
    'include': 'trip,schedule',
    'filter[stop]': 'place-north',
    'filter[route_type]': '2'
}


def index(request):
    r = requests_api.get(FETCH_PREDICTIONS_URI, params=params)
    data_object = r.json()['data']
    included_object = r.json()['included']

    m_time = pytz.timezone('America/New_York')

    destinations = list()
    statuses = list()
    arrival_times = list()
    train_names = list()
    trip_ids_buffer = list()

    for _ in data_object:
        try:
            trip_ids_buffer.append(_['relationships']['trip']['data']['id'])
        except Exception:
            trip_ids_buffer.append('-')

    for _ in data_object:
        try:
            statuses.append(_['attributes']['status'])
        except Exception:
            statuses.append('-')

    for _ in included_object:
        if 'trip' == _['type']:
            for __ in trip_ids_buffer:
                try:
                    if __ == _['id']:
                        destinations.append(_['attributes']['headsign'])
                except Exception:
                    destinations.append('-')

            for __ in trip_ids_buffer:
                try:
                    if __ == _['id']:
                        train_names.append(_['attributes']['name'])
                except Exception:
                    train_names.append('-')

        if 'schedule' == _['type']:
            for __ in trip_ids_buffer:
                try:
                    if __ == _['relationships']['trip']['data']['id'] and _['attributes']['arrival_time'] is not None:
                        arrival_time = datetime.datetime.strptime(_['attributes']['arrival_time'],'%Y-%m-%dT%H:%M:%S%f%z')
                        stripped = arrival_time.strftime('%I:%M %p')
                        arrival_times.append(stripped)
                except Exception:
                    arrival_times.append('-')

    __date = datetime.datetime.now(m_time)
    _date = __date.strftime('%d %b %Y')
    _time = __date.strftime('%H:%M:%S')

    context = {
        'destinations': destinations,
        'statuses': statuses,
        'train_names': train_names,
        'arrival_times': arrival_times,
        'date': _date,
        'time': _time
    }

    return render(request, 'index.html', context)
