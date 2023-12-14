from bardapi import Bard
import sys
import random
import os
import itertools
import requests
import csv
import json
import re
os.environ['_BARD_API_KEY'] = "YOUR_BARD_API_KEY"


def Comment(file_path):
    session = requests.Session()

    session.headers = {
        "Host": "bard.google.com",  # Specify the server hostname
        "X-Same-Domain": "1",  # Inform the server that requests are from the same domain
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",  # Provide a user agent identifier
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",  # Specify the content type for form data
        "Origin": "https://bard.google.com",  # Indicate the origin of the request
        "Referer": "https://bard.google.com/",  # Set the referrer URL
    }

    session.cookies.set("__Secure-1PSID", os.getenv("_BARD_API_KEY"))

    bard = Bard(token=os.environ['_BARD_API_KEY'], session=session, timeout=30)

    with open(file_path, 'r') as code_file:
        code = code_file.read()

    prompt = "Comment the code above"
    final_message = code + "\n" + prompt

    try:
        answer = bard.get_answer(final_message)
        final_answer = answer['content'].split("\n")
    except Exception as e:
        print(e)
        return []

    return final_answer


