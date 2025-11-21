# Using any programming language, read an input file and parse the strings to count how many times an email address is found.

import re
from collections import Counter

emails = {}


def find_emails_in_file(filepath):
    """
    Finds and returns a list of all email addresses found in a given file.
    """
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails_found = []

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            for line in file:
                emails_found = re.findall(email_pattern, line)
                for email in emails_found:
                    emails.setdefault(email, 0)
                    emails[email] += 1
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return emails


# Example usage:
file_path = "emails.txt"  # Replace with the actual path to your file
found_emails = find_emails_in_file(file_path)
print(found_emails)
