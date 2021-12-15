from datetime import datetime, date
import pytest
from unittest.mock import patch, MagicMock



from main import greet, greet_with_date

def test_greeting():
    assert greet() == "Good morning"


def test_is_christmas():
    with patch('datetime.datetime') as mock_date:
        mock_date.now.return_value = datetime.strptime("21-12-25", "%y-%m-%d") #datetime(2021, 12, 25)
        #mock_date.side_effect = lambda *args, **kw: date(*args, **kw)

    assert greet() == "Merry Christmas!"

def test_is_christmas_with_date():
    assert greet_with_date(datetime.strptime("21-12-24", "%y-%m-%d")) == "Merry Christmas!"
    
    