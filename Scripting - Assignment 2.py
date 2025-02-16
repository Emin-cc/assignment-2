import pyautogui
import time
import subprocess

# Opens Notepad, through the subprocess module. 
def open_notepad():
    try:
        subprocess.Popen("notepad.exe")
        print("Notepad is opened.")
    except FileNotFoundError:
        print("Notepad can't be opened.")

# This will hit the space bar every 5 seconds. 
def keep_awake():
    try:
        print("Press Ctrl+C to stop.")
        while True:
            pyautogui.press('space')  # Presses Space bar
            print("Space bar pressed.")
            time.sleep(5) # 5 second wait
    except KeyboardInterrupt:
        print("\nProgram stopped by the user.")

if __name__ == "__main__":
    open_notepad()
    keep_awake()
