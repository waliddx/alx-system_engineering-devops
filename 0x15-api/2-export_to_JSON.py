#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to JSON format.
"""

import json
import requests
import sys

def export_todo_list_to_json(user_id):
    """
    Exports TODO list information for the specified user ID to JSON format.
    """
    url = "https://jsonplaceholder.typicode.com/"
    try:
        user_response = requests.get(url + "users/{}".format(user_id))
        user_response.raise_for_status()  # Raise an error for non-200 status codes
        user = user_response.json()
        username = user.get("username")
        
        todos_response = requests.get(url + "todos", params={"userId": user_id})
        todos_response.raise_for_status()
        todos = todos_response.json()

        with open("{}.json".format(user_id), "w") as jsonfile:
            json.dump({
                user_id: [{
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                    "username": username
                } for todo in todos]
            }, jsonfile, indent=4)

    except requests.RequestException as e:
        print("Error exporting data:", e)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <user_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]
    export_todo_list_to_json(user_id)
    print("TODO list for user {} exported to {}.json".format(user_id, user_id))

