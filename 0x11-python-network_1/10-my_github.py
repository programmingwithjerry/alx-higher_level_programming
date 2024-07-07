
#!/usr/bin/python3
"""
   Python script that takes GitHub credentials (username
   and personal access token) and uses the GitHub API to
   display the user ID.

   The first argument is the username and the second argument
   is the personal access token.
"""
import requests
import sys


if __name__ == "__main__":
    # Get the username and personal access token from the
    # command-line arguments
    username = sys.argv[1]
    token = sys.argv[2]

    # GitHub API URL for the authenticated user
    url = "https://api.github.com/user"

    # Send a GET request to the GitHub API with Basic Authentication
    response = requests.get(url, auth=(username, token))

    # Check if the response is valid and contains the user ID
    if response.status_code == 200:
        # Parse the response as JSON and get the user ID
        user_info = response.json()
        print(user_info.get("id"))
    else:
        # If the response is not valid, print an error message
        print("Error:", response.status_code)
