#!/usr/bin/python3
"""Module 1-top_ten
Queries the Reddit API and prints the titles of the first 10 hot posts."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a subreddit."""
    headers = {'User-Agent': 'alu-scripting/1.0'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return  # silently return for invalid subreddit

        children = response.json().get('data', {}).get('children', [])

        for post in children:
            title = post.get('data', {}).get('title')
            if title:
                print(title)

    except Exception:
        return  # silently fail
