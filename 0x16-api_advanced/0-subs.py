#!/usr/bin/python3
''' Making an API call to a subreddit to get total subscribers '''

import requests
import sys


def number_of_subscribers(subreddit):
    ''' Retrieves number of subscribers of a given subreddit '''

    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # request with custome user agent
    response = requests.get(url, headers={'User-Agent': 'chrome/1.0'})

    # ensure response successful / valid subreddit
    if response.status_code != 200:
        return 0

    # parse response content into a python dictionary
    subreddit_info = response.json()

    # retrieve subscribers from the dictionary
    subscribers = subreddit_info['data']['subscribers']

    return subscribers
