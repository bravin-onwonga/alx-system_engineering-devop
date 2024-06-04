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
        check = requests.head(url, allow_redirects=False)
        check.raise_for_status()
        res = requests.get(url)
        n = int(res.json().get('data').get('subscribers'))
        return n
    except Exception:
        return 0
