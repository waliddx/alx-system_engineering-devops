#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    if not isinstance(subreddit, str):
        return 0
    
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/YourRedditUsername)'}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            subscribers = data.get("data", {}).get("subscribers", 0)
            return subscribers
        else:
            return 0
    except requests.RequestException as e:
        print(f"Request error occurred: {e}")
        return 0
    except ValueError as e:
        print(f"Error decoding JSON response: {e}")
        return 0

if __name__ == '__main__':
    subreddit = input("Enter subreddit name: ")
    subscribers = number_of_subscribers(subreddit)
    print(f"Number of subscribers in r/{subreddit}: {subscribers}")

