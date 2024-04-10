#!/usr/bin/python3
''' Making an API call to a subreddit to get total subscribers '''

import requests
import sys


def number_of_subscribers(subreddit):
    ''' Retrieves number of subscribers of a given subreddit '''

    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # http request with custom user agent
    custom_agent = {'User-Agent':  'chrome/1.0'}
    response = requests.get(url, headers=custom_agent, allow_redirects=False)

    # ensure response successful / valid subreddit
    if response.status_code == 200:
        # parse JSON response to python dictionary
        subreddit_info = response.json()
        # retrieve subscribers from the dictionary response
        subscribers = subreddit_info['data']['subscribers']
        return subscribers
    else:
        # invalid subreddits or request fails
        return 0
