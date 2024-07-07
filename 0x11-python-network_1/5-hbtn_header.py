#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL, and displays
the value of the X-Request-Id variable found in the response header.

Usage: ./script.py <URL>
"""
import requests
import sys


def fetch_x_request_id(url):
    """
    Sends a request to the URL and prints the value of the
    X-Request-Id header.

    Args:
        url (str): The URL to send the request to.
    """
    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)


# Main entry point of the script
if __name__ == "__main__":
    # The URL to be fetched is passed as the first command line argument
    url = sys.argv[1]
    
    # Call the function to fetch and print the 'X-Request-Id'
    fetch_x_request_id(url)
