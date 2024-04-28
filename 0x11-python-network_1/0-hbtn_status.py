#!/usr/bin/python3

import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    status = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(status)))
    print("\t- content: {}".format(status))  # Keep the response as bytes
    # Decode for utf8
    print("\t- utf8 content: {}".format(status.decode('utf-8')))
