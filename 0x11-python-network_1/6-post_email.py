#!/usr/bin/python3
"""
   Python script that takes in a URL and an email address,
   sends a POST request to the passed URL with the email as a
   parameter, and displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    # The URL to be fetched is passed as the first command line argument
    url = sys.argv[1]
    
    # The email to be sent is passed as the second command line argument
    email = sys.argv[2]
    
    # Create a dictionary with the email parameter
    data = {'email': email}
    
    # Send a POST request to the provided URL with the email parameter
    response = requests.post(url, data=data)
    
    # Display the body of the response (decoded in utf-8)
    print(response.text)
