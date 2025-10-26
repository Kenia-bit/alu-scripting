#!/usr/bin/python3
"""Module 1-top_ten
Queries the Reddit API and prints the titles of the first 10 hot posts."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a subreddit."""
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return  # do not print anything for invalid subreddit

        json_data = response.json()
        children = json_data.get('data', {}).get('children', [])

        for post in children:
            title = post.get('data', {}).get('title')
            if title:
                print(title)

    except Exception:
        return  # silently fail for invalid subreddit
