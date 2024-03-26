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
    overall = requests.get("{}users/".format(url)).json()
    for uid in range(1, (len(overall)+1)):
        x = requests.get("{}users/{}".format(url, uid)).json()
        y = requests.get("{}todos?userId={}".format(url, uid)).json()
        z = requests.get(
                "{}todos?userId={}&completed=true".format(url, uid)).json()

        with open("todo_all_employees.json", "a") as data_file:
            json.dump({
                uid:
                [{
                    "task": tasks.get("title"),
                    "completed": tasks.get("completed"),
                    "username": x.get("username")
                    } for tasks in y]
                }, data_file)
