#!/bin/bash
# This script
curl -s -i -X allow "$1" | grep Allow: | cut -d " " -f 2
