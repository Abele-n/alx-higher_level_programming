#!/bin/bash
#script that takes in a URL request and displays all the HTTP methods
curl -s -I -X OPTIONS "$1" | grep 'Allow:' | cut -f2- -d ' '
