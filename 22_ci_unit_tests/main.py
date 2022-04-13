from datetime import datetime
from datetime import date

def func():
    print("Hello")


def greet():
    current_date = datetime.now()
    print(current_date)
    return greet_with_date(current_date)

def greet_with_date(date):
    if date.month == 12 and date.day >= 24 and date.day <= 26:  
        return "Merry Christmas!"
    return "Good morning"
