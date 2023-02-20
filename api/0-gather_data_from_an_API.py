#!/usr/bin/python3
"""my_module"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos"
    user_id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id)).json()
    user_name = user.get("username")
    todos = requests.get(url, params={"userId": user_id}).json()
    with open("{}.csv".format(user_id), "w") as f:
        for todo in todos:
            f.write('"{}","{}","{}","{}"\n'.format(user_id, user_name,
                                                   todo.get("completed"),
                                                   todo.get("title")))
    print("Done")
