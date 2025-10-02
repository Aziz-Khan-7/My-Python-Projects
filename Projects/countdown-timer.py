# Python countdown timer program

import time

print("Welcome to the Simple countdown timer program in Python")
print("-----")
name = input("Please enter your full name: ")
print("-----")
print(f"Hello {name}")

print("-----")
my_time = int(input("Enter the time in seconds: "))
print("-----")

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("-----")
print("TIME'S UP!")
