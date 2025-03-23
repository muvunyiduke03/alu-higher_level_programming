#!/bin/bash
# sends a GET request to the given URL and displays the body only for a 200 status code
curl -sL -w "%{http_code}" "$1" -o temp_body \ { read code; if [ "$code" = "200" ]; then cat temp_body; fi; rm -f temp_body; }

