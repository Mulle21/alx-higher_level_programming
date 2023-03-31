#!/usr/bin/python3
"""Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
if __name__ == "__main__":
    import requests
    import sys

    url = "https://api.github.com/octocat"
    header = "Authorization: Bearer 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"
    header = "X-GitHub-Api-Version: 2022-11-28"
    sys.argv[1]
    passwd = sys.argv[2]
    data_res = requests.get(url, auth=(user, passwd))

    try:
        data_json = data_res.json()
        print(data_json["id"])
    except Exception:
        print("None")
