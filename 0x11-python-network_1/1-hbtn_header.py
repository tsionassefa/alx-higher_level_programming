#!/usr/bin/python3
""" script that take URL,send a request,and display the value """
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(response.headers.get('X-Request-Id'))
