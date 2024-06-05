#!/usr/bin/python3
"""
Find the top ten hotest posts of a subreddit
"""

import requests


def top_ten(subreddit):
    """Send a requests to find top ten posts of a subreddit
    """
    if subreddit is None:
        print("None")
        return
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    try:
        res = requests.get(url, allow_redirects=False, params={'limit': '10'})
        if res.status_code == 200:
            my_lst = res.json().get('data').get('children')

            if not (len(my_lst)):
                print("None")
                return

            for dict in my_lst:
                print(dict.get('data').get('title'))
        return
    except Exception:
        print("None")
        return
