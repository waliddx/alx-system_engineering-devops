#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.
"""

import requests
import sys

def get_todo_list(user_id):
    """
    Retrieves TODO list information for the specified user ID.
    """
    url = "https://jsonplaceholder.typicode.com/"
    try:
        user_response = requests.get(url + "users/{}".format(user_id))
        user_response.raise_for_status()  # Raise an error for non-200 status codes
        user = user_response.json()
        
        todos_response = requests.get(url + "todos", params={"userId": user_id})
        todos_response.raise_for_status()
        todos = todos_response.json()

        completed = [todo.get("title") for todo in todos if todo.get("completed")]
        return user, completed

    except requests.RequestException as e:
        print("Error fetching data:", e)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <user_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]
    user, completed_tasks = get_todo_list(user_id)

    print("Employee {} has completed {}/{} tasks:".format(user.get("name"), len(completed_tasks), len(completed_tasks) + len(user.get("todos"))))
    for task in completed_tasks:
        print("\t", task)

