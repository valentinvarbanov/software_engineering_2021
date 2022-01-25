import requests

def weak_passwords(password):
    weak = ['12345', 'qwerty', 'password', 'asdf']
    if password in weak:
        return True
    return False

def letters_password(password):
    return any(c.isalpha() for c in password)

def special_letters_password(password):
    special_characters = "?!*%$@" #""!@#$%^&*()-+?_=,<>/""

    if any(c in special_characters for c in password):
        return True

    return False


def size_password(password):
    if len(password) > 8 :
        return True
    return False


def check_password(password):
    if weak_passwords(password):
        return 0.0

    complexity = 0.0

    if letters_password(password):
        complexity += 0.25

    if special_letters_password(password):
        complexity += 0.25


    if size_password(password):
        complexity += 0.5

    return complexity



response = requests.get('https://passwordinator.herokuapp.com/generate').json()
# print(response)

password = response['data']
print(password)
print(check_password(password))
