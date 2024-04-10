#!/usr/bin/python3
'''
recursive function that queries the Reddit API, parses the title of all hot
articles, and prints a sorted count of given keywords (case-insensitive,
delimited by spaces
'''
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100, 'after': after}

    custom_agent = {'User-Agent': 'chrome/1.0'}

    # Make a GET request to the URL
    response = requests.get(url, headers=custom_agent, params=params)

    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        # Iterate over each post
        for post in posts:
            title = post['data']['title'].lower()
            # Count occurrences of keywords
            for word in word_list:
                if word.lower() in title:
                    counts[word.lower()] = counts.get(word.lower(), 0) + 1

        # Get the ID of the last post for pagination
        after = data.get('data', {}).get('after')

        # Recursively call count_words with the next page of posts
        if after is not None:
            count_words(subreddit, word_list, after, counts)
        else:
            # Print the sorted counts
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
            else:
                # If the subreddit is invalid, print nothing
                return
