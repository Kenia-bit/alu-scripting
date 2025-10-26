#!/usr/bin/python3
"""Module 3-count: Recursively queries the Reddit API and counts keyword occurrences in hot post titles."""

import requests


def count_words(subreddit, word_list, hot_list=None, after=None):
    """
    Recursively count occurrences of keywords in the titles of all hot articles
    for a subreddit.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyRedditApp/1.0"}
    params = {"after": after, "limit": 100}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return

        data = response.json().get("data", {})
        children = data.get("children", [])
        for post in children:
            title = post.get("data", {}).get("title", "")
            if title:
                hot_list.append(title)

        after = data.get("after")
        if after:
            return count_words(subreddit, word_list, hot_list, after)

        # Count keywords
        counts = {}
        normalized_words = [w.lower() for w in word_list]
        for word in normalized_words:
            counts[word] = 0

        for title in hot_list:
            words_in_title = title.lower().split()
            for word in normalized_words:
                counts[word] += words_in_title.count(word)

        # Remove words with 0 count
        counts = {k: v for k, v in counts.items() if v > 0}

        # Sort: descending count, then alphabetically
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

        # Print results
        for k, v in sorted_counts:
            print(f"{k}: {v}")

    except Exception:
        return
