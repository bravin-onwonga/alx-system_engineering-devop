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
    url = "https://reddit.com/r/{}/hot.json".format(subreddit)

    try:
        check = requests.head(url, allow_redirects=False)
        check.raise_for_status()
        res = requests.get(url, params={'limit': '10'})
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
