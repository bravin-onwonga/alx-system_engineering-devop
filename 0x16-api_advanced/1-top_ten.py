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