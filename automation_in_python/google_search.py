import webbrowser ,pyautogui
from time import sleep
import speect_text
def googlesearch():
    x = speect_text.usemic("which song you want to play", "")
    x = x.split()
    xde = ""
    count = 1
    for i in x:
        if count == len(x):
            xde+= i
        else:
            xde += i + "+"
        count += 1
##mero microphone ma activity dekhaudai xa
    print(xde)
    webbrowser.open(f"https://www.google.com/search?q={xde}")
"""    sleep(2)
    google_search = speect_text.usemic("what do you want to search" , "")
    pyautogui.write(google_search)
    pyautogui.press("enter")
    speect_text.say(google_search)"""
