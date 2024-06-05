#!/usr/bin/python3
"""
Recursively queries the Reddit API
"""

import requests


def count_words(subreddit, word_list=[], my_dict={}, after=None):
    """
    Recursively sends requests to find the top posts of a subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'alx_task'}

    try:
        params = {'after': after}
        res = requests.get(url, headers=headers, params=params, allow_redirects=False)
        data = res.json().get('data')
        new_dict = {}

        if not data or not data.get('children'):
            if (my_dict):
                my_dict = dict(
                    sorted(my_dict.items(),
                           key=lambda item: (-item[1], item[0])))
                print_dict(my_dict, list(my_dict.keys()), 0)
            return

        my_lst = data.get('children')
        str = ""
        str = add_titles(my_lst, 0, str).lower()
        new_dict = populate_dict(new_dict, 0, word_list)

        new_dict = count_in_str(new_dict, str, 0, word_list)

        my_dict = update_dict(
            my_dict, new_dict, list(new_dict.keys()), 0, word_list)
        if not data.get('after'):
            if (my_dict):
                my_dict = dict(
                    sorted(my_dict.items(),
                           key=lambda item: (-item[1], item[0])))
                print_dict(my_dict, list(my_dict.keys()), 0)
            return
        return (count_words(subreddit, word_list, my_dict, data.get('after')))
    except Exception as e:
        print("Error: {}".format(e))
        return None


def add_titles(lst, counter=0, str=""):
    """Recursively adds the titles to the list"""
    if counter == len(lst):
        return str
    str = str + lst[counter].get('data').get('title')
    return (add_titles(lst, counter + 1, str))


def populate_dict(new_dict, counter, word_list):
    """Adds keywords to the dictionary"""
    if (counter == len(word_list)):
        return new_dict
    new_dict[word_list[counter].lower()] = 0
    return (populate_dict(new_dict, counter + 1, word_list))


def count_in_str(new_dict, str, counter, word_list):
    """Counts the occurence of a word in a string"""
    if (counter == len(word_list)):
        return new_dict
    key = word_list[counter].lower()
    new_dict[key] = str.count(key)
    return (count_in_str(new_dict, str, counter + 1, word_list))


def update_dict(my_dict, new_dict, lst_keys, counter, word_list):
    if (counter == len(lst_keys)):
        return my_dict
    if len(my_dict) == 0:
        my_dict = populate_dict(my_dict, 0, word_list)
    key = lst_keys[counter]
    curr_value = my_dict[key]
    my_dict[key] = curr_value + new_dict[key]
    return (update_dict(my_dict, new_dict, lst_keys, counter + 1, word_list))


def print_dict(my_dict, lst_keys, counter):
    if counter == len(lst_keys):
        return
    key = lst_keys[counter]
    str = "{}: {}".format(key, my_dict[key])
    print(str)
    return (print_dict(my_dict, lst_keys, counter + 1))
