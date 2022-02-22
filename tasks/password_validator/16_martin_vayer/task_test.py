# task_test.py

from task import check_pass

common_passes = { '12345', 'qwerty', 'password', 'asdf'}


def test_password_matches():
    for common_pass in common_passes:
    	assert check_pass(common_pass) == 0.0

def test_only_letters():
	only_letter_password = "elsys"
	assert check_pass(only_letter_password) == 0.25

def test_letter_and_special_char():
	letter_and_special_char_password = "el$y$"
	assert check_pass(letter_and_special_char_password) == 0.5

def test_letter_and_more_than_8():
	letter_and_more_than_8_password = "elsyselsys"
	assert check_pass(letter_and_more_than_8_password) == 0.75

def test_letter_and_special_char_and_more_than_8():
	letter_and_special_char_and_more_than_8_password = "el$y$el$y$"
	assert check_pass(letter_and_special_char_and_more_than_8_password) == 1.0