#!/bin/bash
#Displays size of the response body size
curl -Is "$1" | grep -w 'Content-Length' | cut -f2 -d ' '
