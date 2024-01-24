#!/bin/bash
# script that sends a request to a URLpassed an an argument
curl -L -s -X HEAD -w "%{http_code}" "$1"
