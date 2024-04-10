#!/usr/bin/python3
''' Making an API call recursively '''

import requests


def recurse(subreddit, hot_list=[], after=None):
    '''
    Recursively queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles of hot articles (default
        is an empty list).
        after (str): The 'after' parameter for pagination (default is None).

        Returns:
              list: A list containing the titles of all hot articles for the
              subreddit, or None if the subreddit is not valid.
    '''
    # Base case: If subreddit is not valid, return None
    if subreddit is None:
        return None

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    # Set a custom User-Agent to avoid errors related to Too Many Requests
    headers = {'User-Agent': 'chrome/1.0'}

    # Parameters for pagination
    params = {'limit': 100, 'after': after}

    # Make a GET request to the URL
    response = requests.get(url, headers=headers, params=params)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        subreddit_info = response.json()
        # Extract the hot posts from the response
        posts = subreddit_info['data']['children']

        # Append the titles of hot posts to the hot_list
        for post in posts:
            hot_list.append(post['data']['title'])

        # Recursive call with the 'after' parameter for pagination
        after = subreddit_info['data']['after']
        if after is not None:
            recurse(subreddit, hot_list, after)
        # Return the hot_list
        return hot_list
    else:
        # Return None if the subreddit is not valid
        return None
