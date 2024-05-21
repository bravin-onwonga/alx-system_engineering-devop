#!/usr/bin/python3
"""
Exports the response to csv format
"""

import json
import requests
import sys


if __name__ == "__main__":
    my_dct = {}
    filename = "todo_all_employees.json"
    url = "https://jsonplaceholder.typicode.com/"

    url_todos = url + "/todos"

    all_users_todos = requests.get(url_todos).json()

    for i in range(1, 11):
        my_lst = []
        url_user = url + "users?id=" + str(i)
        user_info = requests.get(url_user).json()
        user_name = user_info[0]['username']
        for user_todos in all_users_todos:
            if user_todos['userId'] == i:
                temp_dict = {
                    'username': user_name,
                    'task': user_todos.get('title'),
                    'completed': user_todos.get('completed')
                }
                all_users_todos.remove(user_todos)
            my_lst.append(temp_dict)
        my_dct[i] = my_lst

    with open(filename, 'w') as f:
        data = json.dumps(my_dct)
        f.write(data)
