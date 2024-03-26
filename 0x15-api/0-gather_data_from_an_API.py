#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID, returns information about his/her TODO list progress.
"""
if __name__ == "__main__":
    import requests
    import sys

    url = "https://jsonplaceholder.typicode.com/"
    x = requests.get("{}users/{}".format(url, sys.argv[1])).json()
    y = requests.get("{}todos?userId={}".format(url, sys.argv[1])).json()
    z = requests.get(
            "{}todos?userId={}&completed=true".format(url, sys.argv[1])).json()

    print(f"Employee {x.get('name')} is done with tasks({len(z)}/{len(y)}):")
    for tasks in z:
        print(f"\t {tasks.get('title')}")
