#!/usr/bin/python3

import sys
import urllib.request
import urllib.parse

req = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(req) as response:
    the_header = response.getheader("X-Request-Id")

print("{}".format(the_header))
