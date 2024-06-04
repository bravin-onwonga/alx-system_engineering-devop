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
    base_url = "https://reddit.com/"

    url = base_url + 'r/{}'.format(subreddit) + '/about.json'

    try:
        res = requests.get(url)
        n = int(res.json().get('data').get('subscribers'))
        return n
    except Exception:
        return 0
