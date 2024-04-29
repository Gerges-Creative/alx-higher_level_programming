#!/usr/bin/python3

from sys import argv
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = argv[1]

    try:
        req = urllib.request.Request(url)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
