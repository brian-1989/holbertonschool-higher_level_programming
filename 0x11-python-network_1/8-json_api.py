#!/usr/bin/python3
""" This script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.

"""

import requests
import sys

if __name__ == "__main__":
    my_dict = {}
    if len(sys.argv) == 1:
        my_dict['q'] = ""
    else:
        my_dict['q'] = sys.argv[1]
    response = requests.post('http://0.0.0.0:5000/search_user', data=my_dict)
    _json = response.json()
    try:
        if _json != {}:
            print("[{}] {}".format(_json['id'], _json['name']))
        else:
            print("No result")
    except():
        print("Not a valid JSON")
