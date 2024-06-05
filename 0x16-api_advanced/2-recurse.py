#!/usr/bin/python3
"""
Recursively queries the Reddit API
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively sends requests to find the top posts of a subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'alx_task'}

    try:
        params = {'after': after}
        res = requests.get(url, headers=headers, params=params, allow_redirects=False)
        data = res.json().get('data')

        if not data or not data.get('children'):
            return hot_list
        my_lst = data.get('children')
        counter = 0
        hot_list = add_titles(my_lst, counter, hot_list)
        if not data.get('after'):
            return hot_list
        return (recurse(subreddit, hot_list, data.get('after')))
    except Exception as e:
        print("Error: {}".format(e))
        return None


def add_titles(lst, counter=0, hot_list=[]):
    """Recursively adds the titles to the list"""
    if counter == len(lst):
        return hot_list
    hot_list.append(lst[counter].get('data').get('title'))
    return (add_titles(lst, counter + 1, hot_list))
