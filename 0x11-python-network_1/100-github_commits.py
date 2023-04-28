#!/usr/bin/python3
""" Lists the 10 most recent commits on a given GitHub repositor """
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    req = requests.get(url)
    commits = req.json()
    try:
        for t in range(10):
            print("{}: {}".format(
                commits[t].get("sha"),
                commits[t].get("commit").get("author").get("name")))
    except IndexError:
        pass
