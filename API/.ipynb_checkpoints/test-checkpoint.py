import requests

BASE = "http://127.0.0.1:5000/"

response1 = requests.get(BASE +"helloworld/deepesh/24") 
print(response1.json())
