import requests
from bardapi.constants import SESSION_HEADERS
from bardapi import Bard
import json
import os

def load_cookie(element_name):
    with open(os.getcwd() + "/" + "bard.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        if isinstance(data, list):
            for item in data:
                if item.get("name") == element_name:
                    return item.get("value")
        return None

_1PSID = load_cookie("__Secure-1PSID")
_1PSIDTS = load_cookie("__Secure-1PSIDTS")
_1PSIDCC = load_cookie("__Secure-1PSIDCC")

print(_1PSID)
print(_1PSIDTS)
print(_1PSIDCC)

