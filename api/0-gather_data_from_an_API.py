#!/usr/bin/python3
"""my_module"""
import requests
import sys
if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        employee_id = int(sys.argv[1])

        # Make the API request
        response_todos = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
        response_user = requests.get(f'https://jsonplaceholder.typicode.com/users?id={employee_id}')

        # Check if the response was successful
        if response_todos.status_code == 200 and response_user.status_code == 200:
            todos = response_todos.json()
            user = response_user.json()[0]

            # Count the number of completed and total tasks
            completed_tasks = [todo for todo in todos if todo['completed']]
            num_completed = len(completed_tasks)
            num_total = len(todos)

            # Print employee name and task progress
            print(f"Employee {user['name']} is done with tasks({num_completed}/{num_total}):")

            # Print list of completed tasks
            for task in completed_tasks:
                print(f"\t{task['title']}")

            # Check if formatting of tasks 1-11 is as expected
            for i, task in enumerate(todos[:11]):
                expected_format = f"Task {i+1} Formatting: OK"
                task_format = f"Task {i+1} Formatting: {'OK' if len(task['title']) <= 50 else 'Incorrect'}"
                assert task_format == expected_format, f"Expected: {expected_format}\nGot: {task_format}"
        else:
            print("An error occurred while retrieving the data.")
    else:
        print("Please enter a valid employee ID as an argument.")
