import requests
from flask import json

BASE = "mynameislakhan"

response1 = requests.post(BASE +"") 
print(response1.json())
