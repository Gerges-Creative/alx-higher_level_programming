#!/usr/bin/python3

from sys import argv
import urllib.parse
import urllib.request

url = argv[1]
values = {'email' : argv[2]}

data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    the_body = response.read().decode('utf-8')
    print(the_body)
