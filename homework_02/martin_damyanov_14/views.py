from django.shortcuts import render
import requests
import json
import datetime
import pytz
import calendar

def api(request):
    cur_time = datetime.datetime.now(pytz.timezone('America/New_York'))
    response = requests.get("https://api-v3.mbta.com/predictions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-departure_time&filter%5Bstop%5D=place-north").json()
    statuses = []
    for status in response['data']:
        statuses.append(status['attributes']['status'])

    context = {
        "cur_year" : cur_time.year,
        "cur_date" : cur_time.day,
        "cur_month" : cur_time.month,
        "cur_weekday" : calendar.day_name[cur_time.weekday()],
        "cur_time" : cur_time.strftime("%H:%M:%S"),
        "statuses" : statuses,
        'data': response,
    }
    return render(request, "timetable.html", context)