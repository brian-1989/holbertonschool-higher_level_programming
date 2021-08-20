#!/usr/bin/python3
""" This script takes in a URL, sends a request to the URL
and displays the body of the response.

"""

import requests
import sys

from requests.models import HTTPError

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
