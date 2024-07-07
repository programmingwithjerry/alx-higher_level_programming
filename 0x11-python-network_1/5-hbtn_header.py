#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL,
and displays
the value of the X-Request-Id variable found in the response header.
"""
import requests
from sys import argv


if __name__ == "__main__":
    """The URL to be fetched is passed as the first
       command line argument
    """
    url = argv[1]

    try:
        # Send a GET request to the provided URL
        response = requests.get(url)
        
        # Print the value of the 'X-Request-Id' header if it exists
        print(response.headers['X-Request-Id'])
    except KeyError:
        # If the 'X-Request-Id' header is not found, do nothing
        pass
