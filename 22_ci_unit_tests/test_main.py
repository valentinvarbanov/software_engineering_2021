from datetime import datetime, date
import pytest
from unittest.mock import patch, MagicMock

from main import greet, greet_with_date

from freezegun import freeze_time

@freeze_time("2021-10-10")
def test_greeting():
    assert greet() == "Good morning"

def test_is_christmass():
    with patch('main.datetime') as mock_date:
        mock_date.now.return_value = datetime.strptime("2021-12-25", "%Y-%m-%d") #datetime(2021, 12, 25)
        
        print(datetime.now())
        assert greet() == "Merry Christmas!"

@freeze_time("2021-12-25")
def test_is_Christmas():
    assert greet() == "Merry Christmas!"


def test_is_christmas_with_date():
    assert greet_with_date(datetime.strptime("21-12-24", "%y-%m-%d")) == "Merry Christmas!"



    