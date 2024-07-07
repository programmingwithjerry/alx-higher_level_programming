#!/usr/bin/python3
"""
Python script that fetches the 10 most recent commits from a given GitHub repository,
displaying the SHA and author name of each commit.

Usage: ./commits_history.py <repository name> <owner name>
"""
import requests
from sys import argv


if __name__ == '__main__':
    # The repository name is passed as the first command-line argument
    repo = argv[1]

    # The owner/username of the repository is passed as the second command-line argument
    owner = argv[2]

    # Define parameters to limit the number of commits fetched to 10
    params = {'per_page': 10}

    # Send a GET request to the GitHub API to fetch commits of the specified repository
    response = requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits',\
            params=params)

    # Parse the response as JSON
    commits = response.json()

    # Loop through the commits and print the SHA and author name of each commit
    for commit in commits:
        sha = commit.get('sha')
        author_name = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author_name}")
