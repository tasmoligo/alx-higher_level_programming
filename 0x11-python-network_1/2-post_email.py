#!/usr/bin/python3
"""
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    mail = {"email": sys.argv[2]}
    fmt = urllib.parse.urlencode(mail).encode("ascii")
    request = urllib.request.Request(url, fmt)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
