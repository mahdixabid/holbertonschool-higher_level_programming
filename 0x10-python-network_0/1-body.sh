#!/bin/bash
# Takes in a URL, sends a GET request to the URL, displays the body of the response
curl -s -L -X GET "$1"
