#!/usr/bin/python3
"""takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    letter_data = {"q": letter}

    response = requests.post(url, data=letter_data)
    try:
        r = response.json()
        if r == {}:
            print("No result")
        else:
            print("{[]} {}".format(r.get("id"), r.get("name")))
    except ValueError:
        print("Not a valid JSON")
