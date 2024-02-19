#!/usr/bin/python3
"""
Exports to-do list information of all employees to JSON format.
"""

import json
import requests

def export_todo_list_all_employees():
    """
    Exports TODO list information of all employees to JSON format.
    """
    url = "https://jsonplaceholder.typicode.com/"
    try:
        users_response = requests.get(url + "users")
        users_response.raise_for_status()  # Raise an error for non-200 status codes
        users = users_response.json()

        todo_data = {}
        for user in users:
            user_id = user.get("id")
            todos_response = requests.get(url + "todos", params={"userId": user_id})
            todos_response.raise_for_status()
            todos = todos_response.json()

            todo_data[user_id] = [{
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username")
            } for todo in todos]

        with open("todo_all_employees.json", "w") as jsonfile:
            json.dump(todo_data, jsonfile, indent=4)

    except requests.RequestException as e:
        print("Error exporting data:", e)

if __name__ == "__main__":
    export_todo_list_all_employees()

