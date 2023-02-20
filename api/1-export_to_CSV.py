#!/usr/bin/python3
"""
Export TODO list data to a CSV file for a given user ID.
"""

import csv
import json
import requests
from sys import argv

if __name__ == "__main__":
    # Request user info by employee ID
    request_employee = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/'.format(argv[1]))

    # Convert user info from JSON to dictionary
    user = json.loads(request_employee.text)

    # Extract the username from the user info dictionary
    username = user.get("username")

    # Request user's TODO list
    request_todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))

    # Dictionary to store task status (completed) in boolean format
    tasks = {}

    # Convert user's TODO list from JSON to a list of dictionaries
    user_todos = json.loads(request_todos.text)

    # Loop through user's TODO list and get completed tasks
    for dictionary in user_todos:
        tasks.update({dictionary.get("title"): dictionary.get("completed")})

    # Export to CSV
    with open('{}.csv'.format(argv[1]), mode='w') as file:
        file_editor = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        for D, B in tasks.items():
            file_editor.writerow([argv[1], username, B, D])
