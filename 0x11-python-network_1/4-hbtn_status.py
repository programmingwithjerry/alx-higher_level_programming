#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status and displays
the body of the response.

The response is displayed in the following format:
    Body response:
        - type: <class 'str'>
        - content: OK
"""
import requests


def fetch_status(url):
    """
    Fetches the URL and prints the body of the response.

    Args:
        url (str): The URL to fetch.
    """
    response = requests.get(url)
    body = response.text

    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)


# Main entry point of the script
if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    fetch_status(url)
