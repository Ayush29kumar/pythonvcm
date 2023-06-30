import pyautogui as p
from time import sleep
import webbrowser
from datetime import datetime

while True:
        k = "ankit"
        webbrowser.open("web.whatsapp.com")
        sleep(7)
        p.press("tab", presses=5)
        for i in k:
            sleep(0.5)
            p.press(i)
        sleep(3)
        p.press("down")
        p.press('enter')
        sleep(2)
        while True :
            p.write("good morning chotu")
            p.press("enter")
            sleep(2)
