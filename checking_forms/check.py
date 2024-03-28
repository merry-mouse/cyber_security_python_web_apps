#!/usr/bin/env python3
import argparse
from urllib.parse import urlparse

import requests
import validators
from bs4 import BeautifulSoup

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

if validators.url(url):
    result_html = requests.get(url).text
    parsed_html = BeautifulSoup(result_html, "html.parser")

    forms = parsed_html.find_all("form")

    for form in forms:
        action = form.get("action")
        if action:
            form_scheme = urlparse(action).scheme
            if form_scheme != "https" and urlparse(url).scheme != "https":
                print("Form is not secure.")
            else:
                print("Form is secure.")
else:
    print("Invalid URL")
