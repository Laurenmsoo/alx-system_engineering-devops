#!/usr/bin/python3
"""Exports to-do list information for all employees to a JSON file."""
import json
import requests

if __name__ == "__main__":
    api_link = "https://jsonplaceholder.typicode.com/"
    users = requests.get(api_link + "users").json()
    todos = requests.get(api_link + "todos").json()

    data = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        tasks = []
        for todo in todos:
            if todo.get("userId") == user_id:
                task_info = {
                    "username": username,
                    "task": todo.get("title"),
                    "completed": todo.get("completed")
                }
                tasks.append(task_info)
        data[user_id] = tasks

    filename = "todo_all_employees.json"
    with open(filename, mode="w") as file:
        json.dump(data, file)

