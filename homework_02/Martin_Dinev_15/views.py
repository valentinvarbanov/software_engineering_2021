from django.shortcuts import render
import requests
import datetime
import pytz
import calendar

def api(request):
    params = {
        "page[offset]" : '0',
        "page[limit]" : '100',
        "sort" : '-arrival_time',
        "filter[stop]" : 'place-north',
        'filter[direction_id]' : '0',
        "filter[route_type]" : '2',
        "include" : 'trip,schedule',
    }

    cur_time = datetime.datetime.now(pytz.timezone('America/New_York'))
    response = requests.get("https://api-v3.mbta.com/predictions", params = params).json()
    dest_times = []
    trip_ids = []
    directions = []
    statuses = []
    vehicle_ids = []
    
    for trip in response['data']:
        trip_ids.append(trip['relationships']['trip']['data']['id'])

    for time in response['included']:
        if time['type'] == 'schedule':
            for id in trip_ids:
                if time['relationships']['trip']['data']['id'] == id:
                    timezone = pytz.timezone('America/New_York')
                    dest_time = datetime.datetime.strptime(datetime.datetime.fromisoformat(str(time['attributes']['departure_time'])).strftime("%Y %m %d %I:%M %p"), "%Y %m %d %I:%M %p")
                    if cur_time < timezone.localize(dest_time):
                        dest_times.append(datetime.datetime.fromisoformat(str(time['attributes']['departure_time'])).strftime("%I:%M %p"))
                    else:
                        trip_ids.remove(id)
    
    for vehicle in response['included']:
        if vehicle['type'] == 'trip':
            for id in trip_ids:
                if vehicle['id'] == id:
                    vehicle_ids.append(vehicle['attributes']['name'])

    for direction in response['included']:
        if direction['type'] == 'trip':
            for id in trip_ids:
                if direction['id'] == id:
                    directions.append(direction['attributes']['headsign'])


    for status in response['data']:
        statuses.append(status['attributes']['status'])

    context = {
        "trips" : trip_ids,
        "cur_year" : cur_time.year,
        "cur_date" : cur_time.day,
        "cur_month" : cur_time.month,
        "cur_weekday" : calendar.day_name[cur_time.weekday()],
        "cur_time" : cur_time.strftime("%I:%M %p"),
        "dest_times" : dest_times,
        "statuses" : statuses,
        "directions" : directions,
        "vehicle_ids" : vehicle_ids,
        'data': response,
    }
    return render(request, "api.html", context)
# Create your views here.
