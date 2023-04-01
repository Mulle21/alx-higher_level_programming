#!/usr/bin/python3
"""Python script that takes 2 arguments in order to solve this challenge.
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://developer.github.com/v3/repos/commits/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    m = requests.get(url)
    commits = m.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("commit").get("sha").get("author").get("name")))
    except IndexError:
        pass
