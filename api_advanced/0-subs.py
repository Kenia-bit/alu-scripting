#!/usr/bin/python3
"""
Module that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit."""
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; MyRedditAPI/1.0)"
    }

    try:
        # Send request without following redirects
        response = requests.get(url, headers=headers, allow_redirects=False)

        # If subreddit doesn't exist or request fails
        if response.status_code != 200:
            return 0

        data = response.json().get("data", {})
        return data.get("subscribers", 0)
    except Exception:
        # In case of network or parsing errors
        return 0
