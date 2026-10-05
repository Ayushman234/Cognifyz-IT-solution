import string

password = input("Enter your password: ")

score = 0

if len(password) >= 8:
    score += 1

if any(ch.islower() for ch in password):
    score += 1

if any(ch.isupper() for ch in password):
    score += 1

if any(ch.isdigit() for ch in password):
    score += 1

if any(ch in string.punctuation for ch in password):
    score += 1

if score == 5:
    print("Password Strength: Very Strong")

elif score == 4:
    print("Password Strength: Strong")

elif score == 3:
    print("Password Strength: Medium")

else:
    print("Password Strength: Weak")