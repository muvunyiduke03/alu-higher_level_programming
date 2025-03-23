#!/bin/bash
# script to get the size of the body of the response for a given URL

if ["$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url="$1"

# Use curl to send a request, then retrieve and display the size of the body
curl -s "$url" -o /dev/null -w "%{size_download}\n"