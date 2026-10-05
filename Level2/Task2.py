import random

try:
    lower = int(input("Enter the starting number: "))
    upper = int(input("Enter the ending number: "))

    if lower >= upper:
        print("Starting number should be smaller than ending number.")

    else:
        secret_number = random.randint(lower, upper)

        while True:
            guess = int(input(f"Guess a number between {lower} and {upper}: "))

            if guess < secret_number:
                print("Too low!")

            elif guess > secret_number:
                print("Too high!")

            else:
                print("Correct! You guessed the number.")
                break

except ValueError:
    print("Invalid input.")