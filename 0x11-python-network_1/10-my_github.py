#!/usr/bin/python3
"""takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    authenticate = requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get(url, auth=authenticate)
    print(response.json().get("id"))
