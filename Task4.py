def calculator():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /, %): ")
        num2 = float(input("Enter second number: "))

        operations = {
            "+": num1 + num2,
            "-": num1 - num2,
            "*": num1 * num2,
            "/": "Error! Division by zero." if num2 == 0 else num1 / num2,
            "%": "Error! Modulus by zero." if num2 == 0 else num1 % num2,
        }

        print("Result:", operations.get(operator, "Invalid Operator"))

    except ValueError:
        print("Invalid input! Please enter numeric values.")


calculator()