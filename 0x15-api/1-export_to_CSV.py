#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID, returns information about his/her TODO list progress.
"""
if __name__ == "__main__":
    import csv
    import requests
    import sys

    url = "https://jsonplaceholder.typicode.com/"
    x = requests.get("{}users/{}".format(url, sys.argv[1])).json()
    y = requests.get("{}todos?userId={}".format(url, sys.argv[1])).json()
    z = requests.get(
            "{}todos?userId={}&completed=true".format(url, sys.argv[1])).json()

    rows = []
    for tasks in y:
        buff = [tasks.get("userId"), f'{x.get("username")}', 
                f'{tasks.get("completed")}', f"{tasks.get('title')}"]
        rows.append(buff)
    with open("{}.csv".format(tasks.get("userId")), "w") as data_file:
        csv_writer = csv.writer(data_file,  quoting=csv.QUOTE_ALL)
        csv_writer.writerows(rows)
