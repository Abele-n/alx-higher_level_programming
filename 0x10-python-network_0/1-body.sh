#!/bin/bash
#script that sends a GET request and displays the response
if [ $(curl -L -s -X HEAD -w "%{http_code}" "$1") == '200' ]; then curl -Ls "$1"; fi
