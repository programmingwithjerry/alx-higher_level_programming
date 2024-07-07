#!/usr/bin/python3
"""
Python script that takes GitHub credentials (username and personal access token)
and uses the GitHub API to display the user ID.
"""
import requests
import sys


if __name__ == "__main__":
    # Get the username and personal access token from the command-line arguments
    username = sys.argv[1]
    token = sys. argv[2]

    try:
        # Send a GET request to the GitHub API with Basic Authentication
        response = requests.get("https://api.github.com/user", auth=(username, token))

        # Parse the response as JSON
        user_info = response.json()

        # Print the user ID from the JSON response
        print(user_info['id'])
    except:
        # If an error occurs (e.g., invalid JSON response or missing 'id'), print 'None'
        print('None')
