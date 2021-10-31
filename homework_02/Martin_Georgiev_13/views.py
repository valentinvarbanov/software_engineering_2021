from django.shortcuts import render
import requests
import pytz
import datetime

def trains(request):

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

    current_time = datetime.datetime.now(pytz.timezone("America/New_York"))
    response = requests.get("https://api-v3.mbta.com/predictions", params = params).json()

    destination_times = []
    trip_ids = []
    directions = []
    statuses = []
    train_ids = []

    for trip in response["data"]:
        trip_ids.append(trip["relationships"]["trip"]["data"]["id"])

    for time in response["included"]:
        if time["type"] == "schedule":
            for id in trip_ids:
                if time["relationships"]["trip"]["data"]["id"] == id:
                    timezone = pytz.timezone("America/New_York")
                    dest_time = datetime.datetime.strptime(datetime.datetime.fromisoformat(str(time["attributes"]["departure_time"])).strftime("%Y %m %d %I:%M %p"), "%Y %m %d %I:%M %p")
                    if current_time < timezone.localize(dest_time):
                        destination_times.append(datetime.datetime.fromisoformat(str(time["attributes"]["departure_time"])).strftime("%I:%M %p"))
                    else:
                        trip_ids.remove(id)

    for train in response["included"]:
        if train["type"] == "trip":
            for id in trip_ids:
                if train["id"] == id:
                    train_ids.append(train["attributes"]["name"])

    for direction in response["included"]:
        if direction["type"] == "trip":
            for id in trip_ids:
                if direction["id"] == id:
                    directions.append(direction["attributes"]["headsign"])

    for status in response["data"]:
        statuses.append(status["attributes"]["status"])

    context = {
        "year" : current_time.year,
        "day" : current_time.day,
        "month" : current_time.month,
        "time" : current_time.strftime("%H:%M:%S"),
        "time" : current_time.strftime("%I:%M %p"),
        "trips" : trip_ids,
        "destination_times" : destination_times,
        "statuses" : statuses,
        "directions" : directions,
        "train_ids" : train_ids,
        "data": response,
    }
    return render(request, "trains.html", context)

