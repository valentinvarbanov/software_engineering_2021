from django.shortcuts import render
import requests, datetime, pytz

# Create your views here.
def index(request):
    massachusetsTime = datetime.datetime.now(pytz.timezone('US/Eastern'))
    
    response = requests.get('https://api-v3.mbta.com/predictions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-departure_time&filter%5Bstop%5D=place-north')
    json_response = response.json()

    destinations = []
    vehicles_statuses = []

    for prediction in json_response['data']:
        try:
            stop_id = prediction['relationships']['stop']['data']['id']
            destination = requests.get(f'https://api-v3.mbta.com/stops/{stop_id}').json()['data']['attributes']['description']
            destinations.append(destination)
        except:
            destinations.append("No destination")
    
    for prediction in json_response['data']:
        try:
            vehicle_id = prediction['relationships']['vehicle']['data']['id']
            status_of_vehicle = requests.get(f'https://api-v3.mbta.com/vehicles/{vehicle_id}').json()['data']['attributes']['current_status']
            vehicles_statuses.append(status_of_vehicle)
        except:
            vehicles_statuses.append("No status")
    
    context = {
        'time': massachusetsTime.strftime("%H:%M"),
        'date': massachusetsTime.strftime("%m - %d - %Y"),
        'day': massachusetsTime.strftime("%A"),
        'data': json_response,
        'destinations': destinations,
        'vehicle_statuses': vehicles_statuses
    }



    return render(request, 'train_station_board.html', context=context)