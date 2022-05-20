import requests
import json
from pprint import pprint

def getInfo(call):
    r = requests.get(call)
    return r.json()

name = "Andy8787"

uuid = "67c27b33ba3d4acf95fb624cdf48d9d4"
uuid_dashed = "67c27b33-ba3d-4acf-95fb-624cdf48d9d4"

API_KEY = "c90502bb-24ad-4f07-9601-98ad77c60dca"

name_link = f"https://api.hypixel.net/player?key={API_KEY}&name={name}"
uuid_link = f"https://api.hypixel.net/player?key={API_KEY}&uuid={uuid_dashed}"

pprint(getInfo(name_link))