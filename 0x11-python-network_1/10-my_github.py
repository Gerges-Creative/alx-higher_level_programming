#!/usr/bin/python3

from sys import argv
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    url ='https://api.github.com/user'
    basic = HTTPBasicAuth(argv[1], argv[2])

    r = requests.get(url, auth=basic)
    print(r.json().get('id'))
