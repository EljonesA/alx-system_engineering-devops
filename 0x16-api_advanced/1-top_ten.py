#!/usr/bin/python3
''' Making an API call to a subreddit to get total subscribers '''

import requests
import sys


def top_ten(subreddit):
    ''' Retrieves number of subscribers of a given subreddit '''

    url = f'https://www.reddit.com/r/{subreddit}/top.json?limit=10'

    # http request with custom user agent
    custom_agent = {'User-Agent':  'chrome/1.0'}
    response = requests.get(url, headers=custom_agent, allow_redirects=False)

    # ensure response successful / valid subreddit
    if response.status_code == 200:
        # parse JSON response to python dictionary
        subreddit_info = response.json()

        # retrieve top 10 posts
        top_posts = subreddit_info['data']['children']
        for post in top_posts:
            print(post['data']['title'])
    else:
        # invalid subreddits or request fails
        print('None')
