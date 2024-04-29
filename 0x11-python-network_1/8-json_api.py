#!/usr/bin/python3
"""
given letter as param, POST to http://0.0.0.0:5000/search_user
usage: ./8-json_api.py [letter only]
"""
from sys import argv
import requests

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'

    if len(argv) == 2:
        payload = {'q': argv[1]}
    else:
        payload = {'q': ""}

    r = requests.post(url, data=payload)

    try:
        res = r.json()
        if dic:
            print("[{}] {}".format(res.get('id'), res.get('name')))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
