#!/usr/bin/python3

"""
A Python script that exports data in the JSON format.
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    # Request user info by employee ID.
    request_employee = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/'.format(argv[1]))
    # Convert json to dictionary.
    user = json.loads(request_employee.text)
    # Extract username.
    username = user.get("username")

    # Request user's TODO list.
    request_todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))
    # Dictionary to store task status (completed) in boolean format.
    tasks = {}
    # Convert json to list of dictionaries.
    user_todos = json.loads(request_todos.text)
    # Loop through dictionary & get completed tasks.
    for dictionary in user_todos:
        tasks.update({dictionary.get("title"): dictionary.get("completed")})

    # Prepare data for export to JSON.
    task_list = []
    for D, B in tasks.items():
        task_list.append({
            "task": D,
            "completed": B,
            "username": username
        })

    json_to_dump = {argv[1]: task_list}
    
    # Export to JSON.
    with open('{}.json'.format(argv[1]), mode='w') as file:
        json.dump(json_to_dump, file)
