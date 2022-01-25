import requests
import json

pass_req = requests.get('https://passwordinator.herokuapp.com/generate')

password = json.loads(pass_req.text)["data"]

# `12345`, `qwerty`, `password` or `asdf`
common_passes = { '12345', 'qwerty', 'password', 'asdf'}

special_characters = {'!','@','#','$','%','^','&','*','(',')','-','+','?','_','=','<','>','/'}


def check_pass(password):
	complexity = 0

	if password in common_passes:
		return 0.0

	for char in password:
		if char in special_characters:
			complexity+=0.25
			break;


	if len(password) > 8:
		complexity+=0.5

	if password.isupper() or password.islower():
		complexity+=0.25

	return complexity

print(check_pass(password))