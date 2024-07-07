#!/usr/bin/python3
"""
   Python script that takes in a letter and sends a POST request to
   http://0.0.0.0:5000/search_user with the letter as a parameter.

   The letter must be sent in the variable q. If no argument is given,
   set q="". If the response body is properly JSON formatted and not
   empty, display the id and name.
   Otherwise:
   - Display "Not a valid JSON" if the JSON is invalid.
   - Display "No result" if the JSON is empty.
"""
import requests
import sys


if __name__ == "__main__":
    # Get the letter from the first command-line argument,
    #or set q="" if no argument is given
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    # Create a dictionary with the letter parameter
    data = {'q': letter}

    # Send a POST request to the specified URL with the letter parameter
    response = requests.post('http://0.0.0.0:5000/search_user', data=data)

    try:
        # Try to parse the response as JSON
        json_response = response.json()

        # Check if the JSON is empty
        if json_response:
            # Display the id and name if the JSON is properly
            # formatted and not empty
            print(f"[{json_response.get('id')}] {json_response.get('name')}")
        else:
            # Display "No result" if the JSON is empty
            print("No result")
    except ValueError:
        # Display "Not a valid JSON" if the JSON is invalid
        print("Not a valid JSON")
