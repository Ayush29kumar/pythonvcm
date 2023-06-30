from datetime import datetime
from time import sleep
import pyautogui , subprocess

import os
cwd = os.getcwd()

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print( current_time)
k = str(current_time)

while True:
    if k == "06:00:00" :
        sleep(0.5)
        import pyautogui
 
        sleep(3)
# Move the mouse to a specific location
        pyautogui.moveTo(3500, 100)

# Perform a left mouse click
        pyautogui.click()
        
"""        password = "20014"
        command = ['sudo', '-S', 'gnome-terminal']

        subprocess.run(command, input=password.encode(), check=True)
        sleep(1)
        pyautogui.write(" sudo -u avin cd /home/avin/PycharmProjects/automation_in_python/ ; sudo -u avin   conda activate /home/avin/anaconda3/envs/automation_in_python; sudo -u avin python3  main.py")
        pyautogui.press("enter")"""
