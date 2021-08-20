#!/usr/bin/python3
""" This script takes in a URL, sends a POST request to the passed URL with the
email as a parameter, and finally displays the body of the response.

"""

import requests
import sys

if __name__ == "__main__":
    data = {}
    data['email'] = sys.argv[2]
    response = requests.post(sys.argv[1], data)
    print(response.text)
