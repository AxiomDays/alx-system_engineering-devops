#!/usr/bin/python3
"""
1-top_ten
script to query the API and return the titles of the first 10 hot posts
"""
import requests


def top_ten(subreddit):
    """
    the function in question
    """
    res = requests.get(
            "https://www.reddit.com/r/{}/hot.json".format(subreddit),
            headers={"User-Agent": "Custom"},
            )

    if res.status_code == 200:
        for post in res.json()['data']['children'][:10]:
            print(post['data']['title'])
    else:
        print(None)
