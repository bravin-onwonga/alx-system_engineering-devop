#!/usr/bin/python3
"""
Exports the response to csv format
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
        url = "https://jsonplaceholder.typicode.com/users/"

        url_user = url + id
        url_todos = url + id + "/todos"

        user_info = requests.get(url_user).json()
        user_todos = requests.get(url_todos).json()

        user_name = user_info.get('username')

        for i in range(len(user_todos)):
            temp_dict = {}
            completed = False
            if user_todos[i].get('completed'):
                completed = True
            title = user_todos[i].get('title')
            temp_dict['task'] = title
            temp_dict['competed'] = completed
            temp_dict['username'] = user_name
            my_lst.append(temp_dict)

        with open(filename, 'w') as f:
            my_dct[id] = my_lst
            data = json.dumps(my_dct)
            f.write(data)
