try:
    terms = int(input("Enter the number of terms: "))

    if terms <= 0:
        print("Please enter a positive number.")

    else:
        first = 0
        second = 1

        print("Fibonacci Sequence:")

        for _ in range(terms):
            print(first, end=" ")
            first, second = second, first + second

except ValueError:
    print("Invalid input.")