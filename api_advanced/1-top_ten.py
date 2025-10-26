#!/usr/bin/python3
"""Module 1-top_ten
Prints the titles of the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a subreddit."""
    headers = {'User-Agent': 'alu-scripting/1.0'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    try:
        r = requests.get(url, headers=headers, allow_redirects=False)
        if r.status_code != 200:
            return

        posts = r.json().get('data', {}).get('children', [])
        for post in posts[:10]:
            title = post.get('data', {}).get('title')
            if title:
                print(title)

    except Exception:
        return
