import re


def is_valid_email(email):
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return bool(re.fullmatch(pattern, email))


email = input("Enter Email: ")

if is_valid_email(email):
    print("Valid Email")
else:
    print("Invalid Email")