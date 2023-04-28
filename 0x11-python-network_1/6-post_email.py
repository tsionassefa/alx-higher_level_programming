#!/usr/bin/python3
""" send a post request to a given url with a given email"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}

    req = requests.post(url, filee=val)
    print(req.text)
