#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL
And displays the value of the X-Request-Id variable
found in the header of the response
"""
if __name__ == "__main__":
    import urllib.request as request
    from sys import argv
    reqst = request.Request(argv[1])
    with request.urlopen(reqst) as r:
        print(r.headers.get('X-Request-Id'))
