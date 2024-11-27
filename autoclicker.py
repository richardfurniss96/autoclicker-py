import pyautogui
import time
import random

def auto_clicker(interval, clicks):
    print("Auto Clicker Started. Press Ctrl+C to stop.")
    try:
        for _ in range(clicks):
            pyautogui.click()  # Perform a single click at the current mouse position
            time.sleep(interval)  # Wait for the specified interval
    except KeyboardInterrupt:
        print("\nAuto Clicker Stopped.")

# Set the interval (in seconds) between clicks and the number of clicks
interval = random.randint(140, 180)/100  # half a second between clicks
clicks = random.randint(100, 114)  # number of clicks to perform

auto_clicker(interval, clicks)
