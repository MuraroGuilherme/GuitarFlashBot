from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)

#def click(x, y):
#    win32api.SetCursorPos((x, y))
#    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
#    time.sleep(0.05)
#    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(1128, 867)[0] == 255:
        keyboard.press_and_release('l')
        
    elif pyautogui.pixel(1039, 865)[0] == 255:
        keyboard.press_and_release('k')
        
    elif pyautogui.pixel(948, 866)[0] == 255:
        keyboard.press_and_release('j')
        
    elif pyautogui.pixel(860, 866)[0] == 255:
        keyboard.press_and_release('s')
        
    elif pyautogui.pixel(769, 865)[0] == 255:
        keyboard.press_and_release('a')

    elif pyautogui.pixel(1145, 700)[2] == 255:
        keyboard.press_and_release('space')




 
        
    
