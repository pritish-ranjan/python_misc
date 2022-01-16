import requests

url = "http://api.randomuser.me/"

response = requests.get(url)

print(response.json())
