#!/usr/bin/python3
"""
0-subs
script to query the API and return the number of subscribers
"""
def number_of_subscribers(subreddit):
    """
    the function in question
    """
    import requests
        
    res = requests.get("https://www.reddit.com/r/{}/about.json".format(subreddit), headers={"User-Agent": "Custom"},)

    if res.status_code == 200:
        return int(res.json().get("data").get("subscribers"))
    else:
        return 0

