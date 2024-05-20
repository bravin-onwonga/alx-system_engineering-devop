#!/usr/bin/python3
"""
Retrieves information about a user TODO list progress based on their ID.
"""

import requests
import sys


if __name__ == "__main__":
    if (len(sys.argv) and int(sys.argv[1]) <= 10):
        count = 0
        id = sys.argv[1]
        url = "https://jsonplaceholder.typicode.com/users/"

        url_posts = url + id + "/posts"
        url_user = url + id
        url_todos = url + id + "/todos"

        user_posts = requests.get(url_posts).json()
        user_user_posts = requests.get(url_user).json()
        url_todos = requests.get(url_todos).json()
        for k in range(len(url_todos)):
            if (url_todos[k].get('completed')):
                count += 1

        total_todos = k + 1
        completed_todos = count
        employee_name = user_user_posts.get('name')
        print("Employee {} is done with tasks({}/{}):".format(
            employee_name, completed_todos,
            total_todos))
        for i in range(len(user_posts)):
            print("\t", user_posts[i].get('title'))
