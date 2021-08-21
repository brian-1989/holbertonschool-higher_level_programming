#!/usr/bin/python3
""" This script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.

"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        obj = {"q": sys.argv[1]}
    else:
        obj = {"q": ""}
    response = requests.post('http://0.0.0.0:5000/search_user', data=obj)
    _json = response.json()
    try:
        if len(_json) > 0:
            print("[{}] {}".format(_json['id'], _json['name']))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
