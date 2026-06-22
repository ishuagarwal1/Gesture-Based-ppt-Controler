import os
import time
import pyautogui

def open_ppt(path):
    os.startfile(path)
    time.sleep(5)
    pyautogui.press("f5")

def next_slide():
    pyautogui.press("right")

def prev_slide():
    pyautogui.press("left")
