#!/usr/bin/python3
""" This script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.

"""

import requests
import sys
from requests.exceptions import HTTPError

if __name__ == "__main__":
    if len(sys.argv) > 1:
        obj = {"q": sys.argv[1]}
    else:
        obj = {"q": ""}
    try:
        response = requests.post('http://0.0.0.0:5000/search_user', data=obj)
        response.raise_for_status()
        _json = response.json()
        if len(_json) > 0:
            print("[{}] {}".format(_json['id'], _json['name']))
        else:
            print("No result")
    except(HTTPError) as error:
        print("Not a valid JSON")
    except Exception as err:
        print("Not a valid JSON")
