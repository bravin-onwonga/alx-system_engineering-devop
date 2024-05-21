#!/usr/bin/python3
"""
Exports the response to json file
"""

import json
import requests
import sys


if __name__ == "__main__":
    if (len(sys.argv) and int(sys.argv[1]) <= 10):
        id = str(sys.argv[1])
        my_dct = {}
        my_lst = []
        filename = id + ".json"
        url = "https://jsonplaceholder.typicode.com/"

        url_user = url + "users?id=" + id
        url_todos = url + "/todos"

        user_info = requests.get(url_user).json()
        all_users_todos = requests.get(url_todos).json()

        user_name = user_info[0]['username']

        for user_todos in all_users_todos:
            if user_todos.get('userId') == int(id):
                temp_dict = {
                    "task": user_todos['title'],
                    "completed": user_todos['completed'],
                    "username": user_name
                }
                my_lst.append(temp_dict)

        with open(filename, 'w') as f:
            my_dct[id] = my_lst
            data = json.dumps(my_dct)
            f.write(data)
