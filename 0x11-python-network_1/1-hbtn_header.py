#!/usr/bin/python3
# sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.

import urllib.request
import sys


if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(request) as response:
        req = response.read()
        print("{}".format(req.headers("X-Request-Id")))
