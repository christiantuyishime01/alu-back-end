#!/usr/bin/python3
"""
Exports data of all employees' TODO lists in JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    url_users = "https://jsonplaceholder.typicode.com/users"
    url_todos = "https://jsonplaceholder.typicode.com/todos"

    users = requests.get(url_users).json()
    todos = requests.get(url_todos).json()

    all_tasks = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        user_tasks = []

    for task in todos:
        if task.get("userId") == user_id:
        user_tasks.append({
            "username": username,
            "task": task.get("title"),
            "completed": task.get("completed")
        })

    all_tasks[user_id] = user_tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)
                                                                                                                            
