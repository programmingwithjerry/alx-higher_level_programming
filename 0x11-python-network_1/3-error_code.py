#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL, and displays
the body of the response (decoded in utf-8).

If an HTTPError occurs, it prints "Error code:" followed by the HTTP status code.

Usage: ./script.py <URL>
"""
import urllib.request
import urllib.error
import sys


def fetch_url(url):
    """
    Sends a request to the URL and prints the body of the response (decoded in utf-8).
    If an HTTPError occurs, prints the error code.

    Args:
        url (str): The URL to send the request to.
    """
    try:
        # Use 'with' statement to ensure the response is properly closed after use
        with urllib.request.urlopen(url) as response:
            # Read and decode the response body
            body = response.read().decode('utf-8')

            # Print the response body
            print(body)
    except urllib.error.HTTPError as e:
        # Print the error code if an HTTPError occurs
        print("Error code:", e.code)


# Main entry point of the script
if __name__ == "__main__":
    # The URL to be fetched is passed as the first command line argument
    url = sys.argv[1]

    # Call the function to fetch the URL and print the response
    fetch_url(url)
