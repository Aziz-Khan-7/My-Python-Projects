# Python countdown timer program

import time

# Collect user name

print("Welcome to the Simple countdown timer program in Python")
name = input("Please enter your full name: ")
print(f"Hello {name}")

# Enter time in seconds

my_time = int(input("Enter the time in seconds: "))

# While loop for entering an invalid time

while my_time <= 0:
    print(f"{my_time} is not a valid time")
    my_time = int(input("Enter the time in seconds: "))

# Timer countdown program (for loop)

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP!")
