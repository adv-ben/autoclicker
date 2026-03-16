import pyautogui
import time

pyautogui.FAILSAFE = True

print("move to position")
time.sleep(3)
print("starting")

while True:
    pyautogui.click()
    time.sleep(0.1)