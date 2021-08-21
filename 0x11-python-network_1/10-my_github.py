#!/usr/bin/python3
""" This script that takes your GitHub credentials (username and password).

"""

import requests
import sys

if __name__ == "__main__":
    try:
        response = requests.get(
            'https://api.github.com/user', auth=(sys.argv[1], sys.argv[2]))
        _json = response.json()
        print(_json['id'])
    except:
        print(None)
