from bardapi import Bard  # Import the Bard API library
import os  # Import the os module for file system operations
import requests  # Import the requests library for making HTTP requests
import json  # Import the json module for working with JSON data

# Set the Bard API key as an environment variable
os.environ['_BARD_API_KEY'] = "dQh7a2VL72hAjugeTpFd5Nbqj6rDSHK1Lyh-tRBnlyY_593F3uD1xFH-UxkCnbyvw1fSsw."


def Comment(file_path):
    # Initialize a requests session to maintain connections and cookies
    session = requests.Session()

    # Set the HTTP headers for the requests to interact with the Bard API
    session.headers = {
        "Host": "bard.google.com",  # Specify the server hostname
        "X-Same-Domain": "1",  # Inform the server that requests are from the same domain
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",  # Provide a user agent identifier
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",  # Specify the content type for form data
        "Origin": "https://bard.google.com",  # Indicate the origin of the request
        "Referer": "https://bard.google.com/",  # Set the referrer URL
    }

    # Set the Bard API key as a cookie in the session for authentication
    session.cookies.set("__Secure-1PSID", os.getenv("_BARD_API_KEY"))

    # Create a Bard instance using the API key and session to interact with the Bard API
    bard = Bard(token=os.environ['_BARD_API_KEY'], session=session, timeout=30)

    # Continuously loop until the user exits or the condition is not met
    while True:
        # Prompt the user to enter a message to determine the action
        message = str(input("Prompt: [COMMENT|DOCUMENT: ] "))

        # Check if the message is "comment" to proceed with code commenting
        if message.lower() == "comment":
            # Read the code from the specified file path
            with open('./gpt.py') as code_file:
                code = code_file.read()  # Read the entire code content

            # Prepare the prompt for Bard by combining code and request
            prompt = "Comment the code above"
            final_message = str(code) + "\n" + prompt  # Concatenate code and prompt

            # Send the request to Bard and get the response using the Bard instance
            try:
                # Call the Bard API and store the response in the 'answer' variable
                answer = bard.get_answer(final_message)

                # Extract the response content from the 'answer' dictionary
                final_answer = answer['content'].split("\n")  # Split response content into lines

                # Return the processed response and indicate success
                return final_answer, True  # Return the response lines and success flag

            except Exception as e:  # Handle any exceptions that occur during API calls
                print(e)  # Print the error message
                return "", False  # Return an empty string and failure flag

        else:
            # If the message is not "comment", return an empty string and False
            return "", False  # Return empty response and failure flag

# Print the greeting message
print("Hello world")

