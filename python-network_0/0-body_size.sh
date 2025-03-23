#!/bin/bash
# Sends a request to the provided URL and gets the size of the response
curl -s "$1" -o /dev/null -w "%{size_download}\n"
