from django.shortcuts import render

# Create your views here.

import requests

def trains(request):

    # maybe we would need additional params
    params = {
        'page[offset]': '0',
        'page[limit]': '50',
        'include': 'trip,schedule',
        'filter[stop]': 'place-north',
        'filter[route_type]': '2', # rail
    }

    response = requests.get('https://api-v3.mbta.com/predictions', params=params).json()

    statuses = []

    for element in response['data']:
        statuses.append(element['attributes']['status'])

    context =  {
        'statuses': statuses
    }

    return render(request, "index_trains.html", context)