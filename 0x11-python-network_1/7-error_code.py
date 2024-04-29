#!/usr/bin/python3
"""
given URL & email as params, display response body utf-8, print error codes
usage: ./7-error_code.py http://0.0.0.0:5000/status_401
"""
from sys import argv
import requests

if __name__ == "__main__":
    try:
        r = requests.get(argv[1])
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(e))
