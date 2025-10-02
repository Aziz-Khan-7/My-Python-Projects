# This is a simple interactive Python project that greets the user, collects their information, and performs basic arithmetic operations based on their status.
# The Project name is: "Random Python Project"

input("Hello and welcome to the: 'Random Python Project', Press enter to continue.")

# Collect user information 

full_name = input("Please enter your full name: ")
age = float(input("Please enter your age: "))
status = input("Please enter your status (student, employed, unemployed): ")

print(f"Hello {full_name}, what would you like to do today? ")

# Conditional responses based on user status

if status.lower() == "student":
    print("As a student, you have access to the Simple calculator.")
elif status.lower() == "employed":
    print("As an employed person, you have access to the  Advanced calculator.")
elif status.lower() == "unemployed":
    print("You are unemployed and cannot access the calculator.")

# Simple calculator functionality

print("Welcome to the Simple Calculator.")

operation = input("Please enter the operation you would like to perform (+, -, *, /): ")

num1 =float(input("Please enter your first number: "))
num2 =float(input("Please enter your second number: "))

# Perform the operation and display the result

if operation == "+":
    print(f"The Answer is: {num1 + num2}")
elif operation == "-":
    print(f"The Answer is: {num1 - num2}")
elif operation == "*":
    print(f"The Answer is: {num1 * num2}")
elif operation == "/":
    print(f"The Answer is: {num1 / num2}")
else:
    print(f"Invalid {operation} please try again")

print("Thank you for using the random python project. Goodbye!")

# End of the project (^_^)
