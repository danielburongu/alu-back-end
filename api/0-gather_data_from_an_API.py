#!/usr/bin/python3
"""my_module"""
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python main.py [employee_id]")
    sys.exit()

employee_id = sys.argv[1]
url = 'https://jsonplaceholder.typicode.com/todos?userId=' + employee_id

response = requests.get(url)
todos = response.json()

if not todos:
    print("User not found")
    sys.exit()

done_tasks = [todo for todo in todos if todo['completed']]
total_tasks = len(todos)

employee_name = todos[0]['userId']

print("Employee Name: {}".format(employee_name))
print("Employee {} is done with tasks({}/{}):".format(employee_name, len(done_tasks), total_tasks))

for task in done_tasks:
    print("\t {}".format(task['title']))
