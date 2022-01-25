from password import *

def test_too_basic():
    """
    Tests 'banned' passwords.
    """
    passwords = ['12345', 'qwerty', 'password', 'asdf']
    
    for p in passwords:
        assert check_password(p) == 0.0

def test_only_letters():
    """
    Tests passwords that only contain letters and are under 8 chars.
    """
    passwords = ["deni", 'deDDDDn', 'elsys']

    for p in passwords:
        assert check_password(p) == 0.25

def test_only_numbers():
    """
    Tests passwords that only contain digits and are under 8 chars.
    """
    passwords = ["11111", '2532']

    for p in passwords:
        assert check_password(p) == 0.0

def test_only_specials():
    """
    Tests passwords that only contain special characters and are under 8 chars.
    """
    passwords = ["!!!!", '???', '****', '%%%%%%%%', '$$$$', '@@@@@']

    for p in passwords:
        assert check_password(p) == 0.25


def test_letters_and_specials():
    """
    Tests passwords that only contain letters and special characters and are under 8 chars.
    """
    passwords = ["das!", 'ds?']

    for p in passwords:
        assert check_password(p) == 0.5

def test_long_only_letters():
    """
    Tests passwords longer than 8 that only contain letters.
    """
    passwords = ["dasdasdasdsada", 'dsdasdadsdab']

    for p in passwords:
        assert check_password(p) == 0.75


def test_long_only_specials():
    """
    Tests passwords longer than 8 that only contain special characters.
    """
    passwords = ["!!!!!!!!!", '@@@@@@@@@@', "@@@@!!%%%%%%%%%%", '$$$$!!!@@']

    for p in passwords:
        assert check_password(p) == 0.75


def test_long_only_digits():
    """
    Tests passwords longer than 8 that only contain digits.
    """
    passwords = ["321312151", '44444444444444444']

    for p in passwords:
        assert check_password(p) == 0.5



def test_complex():
    """
    Tests complex passwords with mix of several of the requirements.
    """
    password = "el$y$"
    assert check_password(password) == 0.5

    password = "elsyselsys"
    assert check_password(password) == 0.75

    password = "el$y$el$y$"
    assert check_password(password) == 1.0

    password = "pishete mi 6"
    assert check_password(password) == 0.75
