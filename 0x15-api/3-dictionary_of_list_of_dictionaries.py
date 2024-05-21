#!/usr/bin/python3
"""
Exports the response to csv format
"""

import json
import requests


if __name__ == "__main__":
    my_dct = {}
    filename = "todo_all_employees.json"
    url = "https://jsonplaceholder.typicode.com/"

    url_todos = url + "/todos"

    all_users_todos = requests.get(url_todos).json()

    for i in range(1, 11):
        my_dct[i] = []

    for user_todos in all_users_todos:
        temp_dict = {}
        id = str(user_todos.get('userId'))
        url_user = url + "users?id=" + id
        user_info = requests.get(url_user).json()
        user_name = user_info[0]['username']
        temp_dict = {
            'username': user_name,
            'task': user_todos.get('title'),
            'completed': user_todos.get('completed')
        }
        my_dct[int(id)].append(temp_dict)

    with open(filename, 'w') as f:
        data = json.dumps(my_dct)
        f.write(data)
