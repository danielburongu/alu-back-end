#!/usr/bin/python3
"""my_module"""
import requests
import sys


if __name__ == "__main__":
    # Get the employee ID from the command line arguments
    employee_id = sys.argv[1]

    # Send a GET request to the API to retrieve the employee details
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = response.json()

    # Extract the employee name from the API response
    employee_name = employee_data['name']

    # Send a GET request to the API to retrieve the employee's todo list
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    todo_data = response.json()

    # Count the number of completed tasks
    num_completed_tasks = sum(1 for todo in todo_data if todo['completed'])

    # Print the employee's progress
    num_total_tasks = len(todo_data)
    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{num_total_tasks}):")

    # Print the titles of the completed tasks
    for todo in todo_data:
        if todo['completed']:
            print(f"\t{todo['title']}")
