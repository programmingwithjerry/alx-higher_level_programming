#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL, and displays
the value of the X-Request-Id variable found in the header of the response.

Usage: ./1-hbtn_header.py <URL>
"""
import urllib.request
import sys


def fetch_x_request_id(url):
    """
    Fetches the URL and prints the value of the X-Request-Id header.

    Args:
        url (str): The URL to send the request to.
    """
    # Use 'with' statement to ensure the response is properly closed after use
    with urllib.request.urlopen(url) as response:
        # Fetch the headers from the response
        headers = response.info()
        # Get the value of the 'X-Request-Id' header
        x_request_id = headers.get('X-Request-Id')
        # Print the value of the 'X-Request-Id' header
        print(x_request_id)

# Main entry point of the script
if __name__ == "__main__":
    # The URL to be fetched is passed as the first command line argument
    url = sys.argv[1]
    # Call the function to fetch and print the 'X-Request-Id'
    fetch_x_request_id(url)
