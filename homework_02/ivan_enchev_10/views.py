from django.shortcuts import render
import requests
import pytz
import datetime

def departure_board(request):

    params = {
        "include": "trip,schedule",
        "filter[stop]": "place-north",
        "filter[direction_id]": "0",
        "filter[route_type]": "2",
        "sort": "-arrival_time",
        "page[offset]": "0",
        "page[limit]": "100",
    }

    trips = []
    trains = []
    directions = []
    destination_times = []
    train_statuses = []

    json_data = requests.get("https://api-v3.mbta.com/predictions", params=params).json()

    for trip_info in json_data["data"]:
        trips.append(trip_info["relationships"]["trip"]["data"]["id"])

    for train_info in json_data["included"]:
        if train_info["type"] == "trip":
            for id in trips:
                if train_info["id"] == id:
                    trains.append(train_info["attributes"]["name"])

    for direction_info in json_data["included"]:
        if direction_info["type"] == "trip":
            for id in trips:
                if direction_info["id"] == id:
                    directions.append(direction_info["attributes"]["headsign"])

    for time_info in json_data["included"]:
        if time_info["type"] == "schedule":
            for id in trips:
                if time_info["relationships"]["trip"]["data"]["id"] == id:
                    destination_times.append(datetime.datetime.fromisoformat(str(time_info["attributes"]["departure_time"])).strftime("%I:%M %p"))

    for status in json_data["data"]:
        train_statuses.append(status["attributes"]["status"])

    date = datetime.datetime.now(pytz.timezone("America/New_York"))
    context = {
        "day": date.day,
        "month": date.month,
        "year": date.year,
        "now": date.strftime("%H:%M:%S"),
        "trips": trips,
        "trains": trains,
        "directions": directions,
        "destination_times": destination_times,
        "train_statuses": train_statuses,
        "data": json_data
    }

    return render(request, "departure_board.html", context=context)
