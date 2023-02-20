#!/usr/bin/python3
"""
    Python script that exports data in the JSON format.
"""

import json
import requests

if __name__ == "__main__":
    # Define the base URL for the API.
    url = "https://jsonplaceholder.typicode.com/"

    # Retrieve the list of users from the API.
    users = requests.get(url + "users").json()

    # Generate a JSON object with the TODO items for all users.
    todos = {
        u.get("id"): [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            }
            for t in requests.get(url + "todos", params={"userId": u.get("id")}).json()
        ]
        for u in users
    }

    # Export the generated JSON object to a file.
    with open("todo_all_employees.json", "b") as json_file:
        json.dump(todos, json_file)
