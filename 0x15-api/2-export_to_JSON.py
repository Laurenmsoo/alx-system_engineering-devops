#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to a JSON file."""
import json
import requests
import sys

if __name__ == "__main__":
    api_link = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    usr = requests.get(api_link + "users/{}".format(user_id)).json()
    todos = requests.get(api_link + "todos", params={"userId": user_id}).json()

    username = usr.get("username")
    filename = "{}.json".format(user_id)

    tasks = []
    for todo in todos:
        task_info = {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
        }
        tasks.append(task_info)

    data = {user_id: tasks}

    with open(filename, mode="w") as file:
        json.dump(data, file)

