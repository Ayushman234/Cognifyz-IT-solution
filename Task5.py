def is_palindrome(text):
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


text = input("Enter a string: ")

if is_palindrome(text):
    print("Palindrome")
else:
    print("Not a Palindrome")