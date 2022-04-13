import requests
import json
import re

def check_password(p):
    score = 0.0
    print(p)
    if p in ['12345', 'qwerty', 'password', 'asdf']: return score

    contains_letters = True if re.search(r"[A-Za-z]", p) is not None else False
    over_8_chars = True if len(p) > 8 else False
    contains_special_characters = True if re.search(r'[?!*%$@]', p) is not None else False

    score += contains_letters * 0.25 + over_8_chars * 0.5 + contains_special_characters * 0.25
    return score

if __name__ == '__main__':
    url = "https://passwordinator.herokuapp.com/generate"
    password = requests.get(url).json()['data']
    print(check_password(password))