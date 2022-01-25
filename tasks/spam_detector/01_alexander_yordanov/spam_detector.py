import requests, json
import re

URL = "https://random-data-api.com/api/users/random_user"
response = requests.get(URL)
data = response.json()
email = data['email']

def detect_spam(email):
    likelyhood = 0    
    domain = email.split("@")[1]
    print("email : " + email)
    print("domain : " + domain)

    if(email == "john@win-supp.com" or email == "windows.support@gmail.com" or email == "today@promo.com"):
        likelyhood = 1

    if(".cn" in domain or ".in" in domain or ".info" in domain):
        print(".cn, .in or .info")
        likelyhood = likelyhood + 0.25

    if(any(map(str.isdigit, email)) == True):
        print("0 - 9")
        likelyhood = likelyhood + 0.25

    
    if((domain.count(".") + domain.count("-")) > 2):
        print(domain.count("."))
        likelyhood = likelyhood + 0.5
    
    return float(likelyhood)

print(detect_spam("example123@ma-il.cn"))