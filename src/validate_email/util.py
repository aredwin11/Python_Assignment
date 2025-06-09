import re

def is_valid_email(s):
    return bool(re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', s))

def filter_mail(emails):
    return list(filter(is_valid_email, emails))
