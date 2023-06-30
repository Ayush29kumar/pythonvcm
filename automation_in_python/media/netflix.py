import webbrowser , pyautogui
from time import sleep
import speect_text

def netflix():
    webbrowser.open("netflix.com")
    sleep(7)
    pyautogui.press('tab', presses=4)
    sleep(0.2)
    pyautogui.press("enter")
    video = speect_text.usemic("want to search for something ?", "")
    print(video)
    pyautogui.press('tab', presses=8)
    sleep(0.2)
    pyautogui.press("enter")
    sleep(0.3)
    pyautogui.write(video)
    pyautogui.press("enter")
    sleep(2)
    pyautogui.press("enter")