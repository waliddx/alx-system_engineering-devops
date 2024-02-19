#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to CSV format.
"""

import csv
import requests
import sys

def export_todo_list_to_csv(user_id):
    """
    Exports TODO list information for the specified user ID to CSV format.
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

        with open("{}.csv".format(user_id), "w", newline="") as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for todo in todos:
                writer.writerow([user_id, username, todo.get("completed"), todo.get("title")])

    except requests.RequestException as e:
        print("Error exporting data:", e)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <user_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]
    export_todo_list_to_csv(user_id)
    print("TODO list for user {} exported to {}.csv".format(user_id, user_id))

