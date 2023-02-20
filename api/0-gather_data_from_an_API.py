#!/usr/bin/python3
"""
    This Python script retrieves a given employee's TODO list and returns the
    progress, including the total number of tasks,
    To run this script, pass an employee ID as an argument.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """
        Request employee information by ID
    """
    request_employee = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/'.format(argv[1]))
    """
        convert response JSON to dictionary
    """
    employee = json.loads(request_employee.text)
    """
        Extract employee name from dictionary
    """
    employee_name = employee.get("name")

    """
        Request employee's TODO list by ID
    """
    request_todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))
    """
        Initialize dictionary to store task status
    """
    tasks = {}
    """
        Convert response JSON to list of dictionaries
    """
    employee_todos = json.loads(request_todos.text)
    """
        Loop through dictionary and get completed tasks
    """
    for dictionary in employee_todos:
        tasks.update({dictionary.get("title"): dictionary.get("completed")})

    """
        Print name, total number of tasks, and completed tasks
    """
    EMPLOYEE_NAME = employee_name
    TOTAL_NUMBER_OF_TASKS = len(tasks)
    NUMBER_OF_DONE_TASKS = len([k for k, v in tasks.items() if v is True])
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for D, B in tasks.items():
        if B is True:
            print("\t {}".format(D))
