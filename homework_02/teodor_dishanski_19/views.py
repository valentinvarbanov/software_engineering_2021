from django.shortcuts import render

from django.http import HttpResponse, response
from django.http.response import JsonResponse

from datetime import datetime as d_t

import requests
import datetime
import pytz

# Create your views here.

def train_board(request) -> HttpResponse:
    current_time = datetime.datetime.now(pytz.timezone('America/New_York'))

    params = {
        'page[offset]': '0',                #   Offset on the number of trains.
        'page[limit]': '10',                #   Maximum number of presented trains.
        'sort': 'departure_time',           #   Sorting the trains by departure time.
        'include': 'schedule,stop,trip',    #   Including schedule, stop and train information.
        'filter[stop]': 'place-north',      #   Filterting the trains only on the current stop.
        'filter[direction_id]': '0',        #   Getting only the trains that will departure.
        'filter[route_type]': '2'           #   Getting only the trains by all the vehicles.
    }

    response = requests.get("https://api-v3.mbta.com/predictions", params=params).json()

    departure_times =   list()
    destinations    =   list()
    trains          =   list()
    tracks          =   list()
    statuses        =   list()

    records    =   {}

    if (response['included']):
        #   We make a record in the dictionary by the id of the current record.

        for record in response['included']:
            records[record['id']] = record


        for prediction in response['data']:
            #   We get the data we need by matching the needed sections by their ids.
            #   The last section (the departure time) we get by the attributes section of
            #   the 'data' or by the schedule we have matched. We are sure there will
            #   be trains, otherwise there will not be any matching, that is why
            #   try / except block become needless in the loop.

            prediction['schedule'] = records[prediction['relationships']['schedule']['data']['id']]
            prediction['stop'] = records[prediction['relationships']['stop']['data']['id']]
            prediction['trip'] = records[prediction['relationships']['trip']['data']['id']]
            prediction['departure'] = prediction['attributes']['departure_time'] or prediction['schedule']['attributes']['departure_time']


        for prediction in response['data']:
            #   We append to the specific list the specific attribute we need.
            #   The number of the track may be more specific because of the code / name
            #   recognition. We decide this problem by getting the platform code
            #   or the platform name if there is no still a decided code for the platform.

            departure_times.append(prediction['departure'])
            destinations.append(prediction['trip']['attributes']['headsign'])
            trains.append(prediction['trip']['attributes']['name'])
            tracks.append(prediction['stop']['attributes']['platform_code'] or prediction['stop']['attributes']['platform_name'])
            statuses.append(prediction['attributes']['status'])


        #   We change the format of all departure times.

        for i in range(len(departure_times)):
            departure_times[i] = departure_times[i][11:19]
            departure_times[i] = d_t.strptime(departure_times[i], "%H:%M:%S").time()
            departure_times[i] = departure_times[i].strftime("%I:%M %p")

        #   We check if the track of the current train is with a number.
        #   If it is not, this means it is still TBD (To Be Decided).

        for i in range(len(tracks)):
            if tracks[i] == "Commuter Rail":
                tracks[i] = "TBD"


        #   We sort the information of the trains by their departure times.
        #   If we do not make the sort in all lists, we will get wrong order.

        for i in range(0, len(departure_times)):
            for j in range(i + 1, len(departure_times)):
                if departure_times[i] > departure_times[j]:
                    departure_time = departure_times[i]
                    departure_times[i] = departure_times[j]
                    departure_times[j] = departure_time

                    destination = destinations[i]
                    destinations[i] = destinations[j]
                    destinations[j] = destination

                    train = trains[i]
                    trains[i] = trains[j]
                    trains[j] = train

                    track = tracks[i]
                    tracks[i] = tracks[j]
                    tracks[j] = track

                    status = statuses[i]
                    statuses[i] = statuses[j]
                    statuses[j] = status

    context = {
        'day': current_time.strftime("%A"),
        'date': current_time.strftime("%m - %d - %Y"),
        'time': current_time.strftime("%H:%M"),

        'data': response,
        'departure_times': departure_times,
        'destinations': destinations,
        'trains': trains,
        'tracks': tracks,
        'statuses': statuses
    }

    return render(request, "train_board.html", context)
