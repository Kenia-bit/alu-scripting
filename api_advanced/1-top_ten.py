#!/usr/bin/python3
"""Module 1-top_ten
Print the titles of the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a subreddit."""
    headers = {'User-Agent': 'alu-scripting/1.0'}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return  # nothing printed for invalid subreddit

        data = response.json().get('data', {})
        children = data.get('children', [])

        # Print exactly up to 10 titles
        for i in range(min(10, len(children))):
            title = children[i].get('data', {}).get('title')
            if title:
                print(title)

    except Exception:
        return
