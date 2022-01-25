from django.shortcuts import render
from django.http import HttpResponse

import requests
import datetime
import pytz


def timetable(request):
    datetime_now = datetime.datetime.now(pytz.timezone('America/New_York'))
    timetable_data = requests.get(
        "https://api-v3.mbta.com/predictions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-departure_time&filter%5Bstop%5D=place-north").json()['data']
    status_array = []

    for i in timetable_data:
        status_array.append(i['attributes']['status'])
    context = {
        "status_array": status_array,
        "timetable_data": timetable_data,
        "year": datetime_now.year,
        "day": datetime_now.day,
        "month": datetime_now.month,
        "weekday": datetime_now.weekday,
        "time": datetime_now.strftime("%H:%M:%S")
    }

    return render(request, "index.html", context)
