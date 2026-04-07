import time

print("Hello, and Welcome to Australia's Best AI Software")

input("Press Enter to continue...")
print("--" * 20)

name = input("Please enter your name: ")
print("--" * 20)

age = input("Please enter your age: ")
print("--" * 20)

email = input("Please enter your email: ")
print("--" * 20)

phone = input("Please enter your phone number: ")
print("--" * 20)

print("Thank you for providing your information. We will use it to create a personalized experience for you.")
print("--" * 20)

print("Loading your personalized experience...")
print("--" * 20)
wait_time = 3
time.sleep(wait_time)  

print("Your personalized experience is ready! Enjoy exploring Australia's Best AI Software, " + name + "!")
print("--" * 20)

print("Would you like to receive updates and news about our software? (yes/no): ")
print("--" * 20)

subscribe = input().lower()
if subscribe == "yes":
    print("Thank you for subscribing! You will receive updates and news about our software.")
else:
    print("No problem! You can always subscribe later if you change your mind.")

print("Thank you for using Australia's Best AI Software. Have a great day, " + name + "!")