# Task 1: Advanced Data Extraction

import re

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"

occupation_container = re.search(r"Occupation: (\w+)", text)
print(occupation_container.group(1))


# Task 2: URL Validator

urls = ["https://example.com", "www.example.com", "http://test.com"]

def validate_url(url):
    url_pattern = r"(https://|http://)\w+\.[a-zA-Z]{2,}"
    if re.match(url_pattern, url):
        return True
    else:
        return False

def validate_urls_list(url_list):
    valid_urls = []
    invalid_urls = []
    for url in url_list:
        if validate_url(url):
            valid_urls.append(url)
        else:
            invalid_urls.append(url)

    print("Valid URLs:", valid_urls)
    print("Invalid URLs:", invalid_urls)

validate_urls_list(urls)