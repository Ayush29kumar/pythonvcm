"""import webbrowser
from random import randint

z= ["youtube" ,"facebook" , "instagram" ,"linkedin" ,"tesla" ,"web.whatsapp","github","gmail" ,"netflix" ,"udemy","twitter","hackerrank","stackoverflow"]
for i in range(0,150):
    k = randint(0,12)
    webbrowser.open("www."+z[k]+".com")"""
import webbrowser as wb
import pyautogui as p
from time import sleep
wb.open("web.whatsapp.com")
sleep(10)
p.press("tab" , presses=5)
p.write("Ankit Gupta Ise")
p.press("enter")
c =0
while True:
    p.write("chotu")
    sleep(0.1)
    p.press("enter")
    c+=1
    if c == 100 :
        break


