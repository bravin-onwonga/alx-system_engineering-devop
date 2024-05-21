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
        user_todos = {}
        filename = id + ".json"
        url = "https://jsonplaceholder.typicode.com/"

        url_user = url + "users?id=" + id
        url_todos = url + "/todos"

        user_info = requests.get(url_user).json()
        all_users_todos = requests.get(url_todos).json()