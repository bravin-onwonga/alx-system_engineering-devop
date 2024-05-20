#!/usr/bin/python3
"""
Exports the response to csv format
"""

import requests
import sys


if __name__ == "__main__":
    if (len(sys.argv) and int(sys.argv[1]) <= 10):
        content = ""
        id = str(sys.argv[1])
        filename = id + ".csv"
        url = "https://jsonplaceholder.typicode.com/users/"

        url_user = url + id
        url_todos = url + id + "/todos"

        user_info = requests.get(url_user).json()
        user_todos = requests.get(url_todos).json()

        employee_name = user_info.get('username')

        for i in range(len(user_todos)):
            completed = "False"
            if user_todos[i].get('completed'):
                completed = "True"
            title = user_todos[i].get('title')
            str = '"{}","{}","{}","{}"\n'.format(
                id, employee_name, completed, title)
            content = content + str

        with open(filename, 'w') as f:
            f.write(content)
