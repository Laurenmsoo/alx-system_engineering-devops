#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    api_link = "https://jsonplaceholder.typicode.com/"
    usr = requests.get(api_link + "users/{}".format(sys.argv[1])).json()
    task = requests.get(api_link + "todos", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in task if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        usr.get("name"), len(completed), len(task)))
    [print("\t {}".format(c)) for c in completed]
