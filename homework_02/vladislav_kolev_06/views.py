from django.shortcuts import render
import requests, datetime, pytz


# Create your views here.
def index(request):
    massachusetsTime = datetime.datetime.now(pytz.timezone('US/Eastern'))
    
    params = {
        'page[offset]': '0',
        'page[limit]': '50',
        'include': 'trip,schedule,stop',
        "sort" : 'departure_time',
        'filter[stop]': 'place-north',
        'filter[route_type]': '2', # rail
        'filter[direction_id]': '0',
    }

    response = requests.get('https://api-v3.mbta.com/predictions', params=params)
    json_response = response.json()

    trips = [] # list of dictionaries

    # getting trip indexes
    for prediction in json_response['data']:
        dict = {}
        dict['id'] = prediction['relationships']['trip']['data']['id']
        dict['stop_id'] = prediction['relationships']['stop']['data']['id']
        trips.append(dict)

    # getting statuses
    for prediction in json_response['data']:
        for index in range(0, len(trips)):
            try:
                trips[index]['status'] = prediction['attributes']['status']
            except:
                trips[index]['status'] = "No status"
    
    # getting destinations, train ids, track numbers and departure times
    for included in json_response['included']:
        if included['type'] == 'trip':
            for index in range(0, len(trips)):
               if included['id'] == trips[index]['id']:
                   # getting destination names
                   try:
                        trips[index]['destination'] = included['attributes']['headsign']
                   except:
                       trips[index]['destination'] = "No info"

                   # getting train ids
                   try:
                       trips[index]['train_id'] = included['attributes']['name']
                   except:
                       trips[index]['train_id'] = "No info"
        # getting departure time
        elif included['type'] == 'schedule':
            for index in range(0, len(trips)):
                if included['relationships']['trip']['data']['id'] == trips[index]['id']:
                    try:
                        departure_time_converted = datetime.datetime.fromisoformat(included['attributes']['departure_time']).strftime('%I:%M %p')
                        trips[index]['date'] = departure_time_converted
                    except:
                        trips[index]['date'] = "No info"
        # getting track number
        elif included['type'] == 'stop':
            for index in range(0, len(trips)):
                if included['id'] == trips[index]['stop_id']:
                    if included['attributes']['platform_code']:
                        trips['track'] = included['attributes']['platform_code']
                    else: 
                        trips[index]['track'] = 'TBD'

    # sorting the list of dictionaries
    trips = sorted(trips, key=lambda trip: trip['date'])
    
    context = {
        'time': massachusetsTime.strftime("%H:%M"),
        'date': massachusetsTime.strftime("%m - %d - %Y"),
        'day': massachusetsTime.strftime("%A"),
        'trips': trips
    }



    return render(request, 'train_station_board.html', context=context)