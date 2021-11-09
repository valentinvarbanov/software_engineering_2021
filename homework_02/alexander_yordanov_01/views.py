from django.http import response
from django.shortcuts import render
from django.http.response import JsonResponse
from django.http import HttpResponse
from requests.models import ContentDecodingError
import requests, json
import datetime, pytz
import itertools

def index(request): 
    now = datetime.datetime.now(pytz.timezone('America/New_York'))
    params = {
        'page[offset]': '0',
        'page[limit]': '50',
        "include": 'trip,schedule',
        'filter[stop]': 'place-north',
        'filter[route_type]': '2'
    }

    response = requests.get("https://api-v3.mbta.com/predictions/", headers={"X-API-Key":"537204397425447493511cec18bfc0fa"}, params=params)

    names = []
    statuses = []
    trips = []
    routes = []
    arrivals = []
    data = response.json()

    for i in data['data']:
        try:
            trips.append(i['relationships']['trip']['data']['id'])
        except:
            trips.append("No info")


    for i in data['data']:
        try:
            status = i["attributes"]["status"]
            statuses.append(status)

        except:
            statuses.append("No status")


    for i in data['included']:
        if i['type'] == "trip":
            for j in trips:
                try:
                    if i['id'] == j:
                        routes.append(i['attributes']['headsign'])
                except:
                    routes.append("No info")

    for i in data['included']:
        if i['type'] == "trip":
            for j in trips:
                try: 
                    if i['id'] == j:
                        names.append(i['attributes']['name'])
                except:
                    names.append("No info")

    for i in data['included']:
        if i['type'] == "schedule": 
            for j in trips:
                try:
                    if i['relationships']['trip']['data']['id'] == j:
                        if i['attributes']['arrival_time']:
                            arrivals.append(i['attributes']['arrival_time'])
                        else:
                            arrivals.append("No arrival time")
                except:
                    arrivals.append("No info")



    content = {
        'time_day': now.strftime("%A"),
        'now_time': now.strftime("%m - %d - %Y"),
        'hour': now.strftime("%I:%M %p"),
        'names': routes,
        'statuses': statuses,
        'vehicles_id': names,
        'arrivals': arrivals
    }

    return render(request, "api.html", context = content)