#!/usr/bin/python3
"""Module 1-top_ten: Queries the Reddit API and prints the titles of the first 10 hot posts for a subreddit."""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a subreddit."""
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "MyRedditApp/1.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return

        posts = response.json().get("data", {}).get("children", [])
        for post in posts:
            title = post.get("data", {}).get("title")
            print(title)

    except Exception:
        print(None)
