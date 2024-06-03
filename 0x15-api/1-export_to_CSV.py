#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to a CSV file."""
import csv
import requests
import sys

if __name__ == "__main__":
    api_link = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    usr = requests.get(api_link + "users/{}".format(user_id)).json()
    tasks = requests.get(api_link + "todos", params={"userId": user_id}).json()

    username = usr.get("username")
    filename = "{}.csv".format(user_id)

    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([user_id, username, task.get("completed"), task.get("title")])

