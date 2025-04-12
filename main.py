import time
import sys

def typewriter(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        # time.sleep(speed)
    print()  # Move to next line

# Ask user for input
user_input = input("Enter some text: ")

# Typewrite the input
typewriter(user_input)
