# Task 1: Code Correction

import re

text = "Contact emails are: john.doe@example.com and jane.doe@example.com."
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

print(emails)


# Task 2: Log File Analysis

log_data = "12-25-2022: @john Logged in. 01-01-2023: @jane Accessed the dashboard."

date_formatted_log = re.sub(r"(\d{2})-(\d{2})-(\d{4})", r"\3-\2-\1", log_data)
user_formatted_log = re.sub(r"@\w+", r"[ANONYMIZED USER]", date_formatted_log)
print(user_formatted_log)