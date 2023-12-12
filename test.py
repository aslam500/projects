# Import the Bard API library
from bardapi import Bard
import sys
import random
# Import the os module for file system operations
#import os
import itertools
# Import the requests library for making HTTP requests
import requests
#import csv
# Import the json module for working with JSON data
import json
#import re
# Set the Bard API key as an environment variable
# This is done to avoid exposing the API key in the code
os.environ['_BARD_API_KEY'] = "YOUR_BARD_API_KEY"


def Comment(file_path):
    """
    This function takes a file path as input and returns the commented code.
    It uses the Bard API to generate comments for the code.

    Args:
        file_path (str): The path to the file containing the code to be commented.

    Returns:
        list[str]: A list of commented code lines.
    """

    # Initialize a requests session to maintain connections and cookies
    # This is done to improve performance and avoid making multiple connections
    session = requests.Session()

    # Set the HTTP headers for the requests to interact with the Bard API
    # These headers provide information about the request and improve communication with the API
    session.headers = {
        "Host": "bard.google.com",  # Specify the server hostname
        "X-Same-Domain": "1",  # Inform the server that requests are from the same domain
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",  # Provide a user agent identifier
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",  # Specify the content type for form data
        "Origin": "https://bard.google.com",  # Indicate the origin of the request
        "Referer": "https://bard.google.com/",  # Set the referrer URL
    }

    # Set the Bard API key as a cookie in the session for authentication
    # This is done to identify the user and provide access to the Bard API
    session.cookies.set("__Secure-1PSID", os.getenv("_BARD_API_KEY"))

    # Create a Bard instance using the API key and session to interact with the Bard API
    # This instance will be used to send requests to the Bard API and receive responses
    bard = Bard(token=os.environ['_BARD_API_KEY'], session=session, timeout=30)

    # Read the code from the specified file path
    # This is done to access the code that needs to be commented
    with open(file_path, 'r') as code_file:
        code = code_file.read()

    # Prepare the prompt for Bard by combining code and request
    # The prompt tells Bard what to do with the provided code
    prompt = "Comment the code above"
    final_message = code + "\n" + prompt

    # Send the request to Bard and get the response using the Bard instance
    # This is done to send the prompt to Bard and receive the generated comments
    try:
        answer = bard.get_answer(final_message)
        final_answer = answer['content'].split("\n")
    except Exception as e:
        print(e)
        return []

    # Return the processed response and indicate success
    return final_answer

# Print the greeting message
print("Hello world")

