
import pyautogui
import time

def type_like_human(text, delay=0.2):
    words = text.split()
    for word in words:
        pyautogui.typewrite(word)
        pyautogui.press('space')
        time.sleep(delay)

# Wait a few seconds so you can switch to your target window
print("You have 5 seconds to click where you want it to type...")
time.sleep(5)

# Paste your copied text here
text_to_type = """
My name is ritesh, and i am the don of nepal
"""

type_like_human(text_to_type, delay=0.3)  # You can tweak delay speed
