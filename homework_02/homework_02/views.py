from django.shortcuts import render
from urllib.request import Request

from . import templates

import requests
import datetime

def timetable(request):
    response = requests.get("https://api-v3.mbta.com/predictions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-departure_time&filter%5Bstop%5D=place-north")
    raw_data = response.json()
    arrivals = []
    destinations = []
    trainNums = []
    statuses = []

    for i in raw_data['data']:
        try:
            arrival = i['attributes']['arrival_time']
            cut = arrival.split('T',1)[1]
            time = cut.split('-')[0]
            arrivals.append(time)
        except:
            arrivals.append("None")

    for i in raw_data['data']:
        try:
            destination = requests.get("https://api-v3.mbta.com/trips/" + i["relationships"]["trip"]["data"]["id"]).json()["data"]["attributes"]["headsign"]
            destinations.append(destination)
        except:
            destinations.append("No destination")

    for i in raw_data['data']:
        try:
            trainNum = requests.get("https://api-v3.mbta.com/vehicles/" + i['relationships']['vehicle']['data']['id']).json()['data']['attributes']['label']
            trainNums.append(trainNum)
        except:
            trainNums.append("No info")

    for i in raw_data['data']:
        try:
            status = i['attributes']['status']
            statuses.append(status)
        except:
            statuses.append("No info")

    now = datetime.datetime.now()
    context = {
        'data': raw_data,
        'arrivals': arrivals,
        'destinations': destinations,
        'trainNums': trainNums,
        'statuses': statuses,
        'day': now.strftime("%A"),
        'date': now.strftime("%m - %d - %Y")
    }

    return render(request, "timetable.html", context=context)