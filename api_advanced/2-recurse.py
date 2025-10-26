#!/usr/bin/python3
"""Module 2-recurse: Recursively queries the Reddit API and returns a list of all hot article titles for a subreddit."""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Return a list of all hot article titles for a given subreddit using recursion.
    If the subreddit is invalid or empty, return None.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyRedditApp/1.0"}
    params = {"after": after, "limit": 100}  # 100 is max Reddit allows per page

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return None

        data = response.json().get("data", {})
        children = data.get("children", [])
        for post in children:
            title = post.get("data", {}).get("title")
            if title:
                hot_list.append(title)

        after = data.get("after")
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list

    except Exception:
        return None
