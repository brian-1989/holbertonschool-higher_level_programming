#!/bin/bash
# This script takes in a URL and displays all HTTP methods.
curl -s -i -X allow "$1" | grep Allow | cut -d " " -f 2-
