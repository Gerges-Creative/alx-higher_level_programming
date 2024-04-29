#!/usr/bin/python3
"""
given URL as parameter, fetch URL and display value from reponse header
usage: ./1-hbtn_header https://intranet.hbtn.io
"""
import sys
import urllib.request

req = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(req) as response:
    the_header = response.getheader("X-Request-Id")

print("{}".format(the_header))
