# Basic Calculator Program

# Ask user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask user to input the operation
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation and display the result
if operation == "+":

    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operation == "-":

    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":

    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    # Check for division by zero
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please use +, -, *, or /.")

# End of the calculator program