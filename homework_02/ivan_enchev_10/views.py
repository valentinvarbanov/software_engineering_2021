from django.shortcuts import render
import requests
import pytz
import datetime

def departure_board(request):
    train_status = []
    json_data = requests.get("https://api-v3.mbta.com/predictions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-departure_time&filter%5Bstop%5D=place-north").json()["data"]

    for status in json_data:
        train_status.append(status["attributes"]["status"])

    date = datetime.datetime.now(pytz.timezone("America/New_York"))
    context = {
        "day": date.day,
        "month": date.month,
        "year": date.year,
        "now": date.strftime("%H:%M:%S"),
        "train_statuses": train_status,
        "data": json_data
    }

    return render(request, "departure_board.html", context=context)
