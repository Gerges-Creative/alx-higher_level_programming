#!/usr/bin/python3

import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    status = response.read()

    print("Body response:")
    print("    - type:", type(status))
    print("    - content:", status)  # Keep the response as bytes
    print("    - utf8 content:", status.decode('utf-8'))  # Decode for utf8
