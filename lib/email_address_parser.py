# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, input_string):
        self.input_string = input_string

    def parse(self):
        # Use a regular expression to find email addresses in the input string
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}\b'
        email_addresses = re.findall(email_pattern, self.input_string)

        return email_addresses



