#!/usr/bin/env python3
import argparse
from urllib.parse import urlparse

import requests
import validators
from bs4 import BeautifulSoup, Comment

parser = argparse.ArgumentParser(description="HTML Vulnerability Analyzer")

parser.add_argument(
    "-v",
    "--version",
    action="version",
    version="%(prog)s 1.0",
)
parser.add_argument("url", type=str, help="URL of HTML to analyze")

args = parser.parse_args()
url = args.url

report = ""

if validators.url(url):
    result_html = requests.get(url).text
    parsed_html = BeautifulSoup(result_html, "html.parser")

    forms = parsed_html.find_all("form")
    comments = parsed_html.find_all(string=lambda text: isinstance(text, Comment))
    password_inputs = parsed_html.find_all("input", {"name": "password"})

    for form in forms:
        action = form.get("action")
        if action:
            form_scheme = urlparse(action).scheme
            if form_scheme != "https" and urlparse(url).scheme != "https":
                report += "Form is not secure.\n"
            else:
                report += "Form is secure.\n"

    for comment in comments:
        if comment.find("key:") > -1:
            report += "Key issue. Key found in HTML, remove immediately!\n"

    for password_input in password_inputs:
        if password_input.get("type") != "password":
            report += "Input Issue: Plaintext password input found. Please change to password type input\n"
else:
    print("Invalid URL")

print(report)
