#!/usr/bin/python3
"""
Script that takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response (decoded in utf-8).

Usage: ./script.py <URL> <email>
"""
import urllib.request
import urllib.parse
import sys

def send_post_request(url, email):
    """
    Sends a POST request to the passed URL with the email as a parameter
    and prints the body of the response decoded in utf-8.

    Args:
        url (str): The URL to send the request to.
        email (str): The email to send as a parameter.
    """
    # Encode the email parameter
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    
    # Create a Request object
    req = urllib.request.Request(url, data=data)
    
    # Use 'with' statement to ensure the response is properly closed after use
    with urllib.request.urlopen(req) as response:
        # Read and decode the response body
        body = response.read().decode('utf-8')
        
        # Print the response body
        print(body)

# Main entry point of the script
if __name__ == "__main__":
    # The URL and email to be used in the POST request are passed as command line arguments
    url = sys.argv[1]
    email = sys.argv[2]
    
    # Call the function to send the POST request and print the response
    send_post_request(url, email)

