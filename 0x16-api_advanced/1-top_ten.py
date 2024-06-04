#!/usr/bin/python3
"""
Find the top ten hotest posts of a subreddit
"""

import requests


def top_ten(subreddit):
    """Send a requests to find top ten posts of a subreddit
    """
    if subreddit is None:
        return
    url = "https://reddit.com/r/{}/hot.json".format(subreddit)

    try:
        check = requests.head(url, allow_redirects=False)
        check.raise_for_status()
        res = requests.get(url)
        my_lst = res.json().get('data').get('children')
        i = 0
        for dict in my_lst:
            if i == 10:
                break
            print(dict.get('data').get('title'))
            i += 1
        return
    except Exception:
        print("None")
        return

