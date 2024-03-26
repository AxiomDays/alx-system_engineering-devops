#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID, returns information about his/her TODO list progress.
"""
if __name__ == "__main__":
    import json
    import requests
    import sys

    url = "https://jsonplaceholder.typicode.com/"
    uid = sys.argv[1]
    x = requests.get("{}users/{}".format(url, sys.argv[1])).json()
    y = requests.get("{}todos?userId={}".format(url, sys.argv[1])).json()
    z = requests.get(
            "{}todos?userId={}&completed=true".format(url, sys.argv[1])).json()

    with open("{}.json".format(uid), "w") as data_file:
        json.dump({
            uid:
            [{
                "task": tasks.get("title"),
                "completed": tasks.get("completed"),
                "username": x.get("username")
                } for tasks in y]
            }, data_file)
