#!/usr/bin/python3
"""
Find the number of subscribers of a subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """Send a request to find number of subsribers

    Returns:
        - number of subscriber
        - otherwise zero
    """
    if subreddit is None:
        return 0
    url = "https://reddit.com/r/{}/about.json".format(subreddit)

    try:
        res = requests.get(url, allow_redirects=False)
        if res.status_code == 200:
            data = res.json().get('data', {})
            return data.get('subscribers', 0)
        return 0
    except Exception:
        return 0
