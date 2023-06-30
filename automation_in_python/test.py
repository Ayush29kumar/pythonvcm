"""import pyautogui
import time
import webbrowser
import pytesseract
import os
os.environ['TESSDATA_PREFIX'] = '/usr/share/tesseract-ocr/4.00/tessdata/'
from PIL import Image

webbrowser.open("youtube.com")
time.sleep(5)
pyautogui.press('tab', presses=4)
time.sleep(0.2)
pyautogui.write("counting stars")
pyautogui.press("enter")
time.sleep(2)
pyautogui.press("enter")

# Send the keyboard shortcut to switch to the next tab
import pyautogui
import time

# Send the keyboard shortcut to switch to the next tab
pyautogui.hotkey('ctrl', 'tab')

# Keep switching to the next tab and checking the title until the target video is found
while True:
    # Take a screenshot of the current tab title
    title_image = pyautogui.screenshot(region=(100, 0, 800, 50))
    title_image.save('tab_title.png')
    # Use OCR to extract text from the screenshot
    gray_image = title_image.convert('L')

    # Use pytesseract to recognize text in the image
    title_text = pytesseract.image_to_string(gray_image)
    print("------------------------------",title_text,"----------------------------------")

    # Check if the title contains 'Counting Stars'
    if 'Counting Stars' in title_text:
        # Close the current tab
        pyautogui.hotkey('ctrl', 'w')
        break  # Exit the loop if the tab is closed
    else:
        # Switch to the next tab
        pyautogui.hotkey('ctrl', 'tab')

    # Wait for a short time to avoid overwhelming the system
    time.sleep(0.5)

    # Capture a screenshot of the tab title

"""

"""from selenium import webdriver

# Open Chrome with a new window
driver = webdriver.Chrome()

# Navigate to each tab and check its title
for tab in driver.window_handles:
    driver.switch_to.window(tab)
    title = driver.title

    # Check if it's a YouTube tab and playing "Escape"
    if "YouTube" in title and "Escape" in title:
        # Close the tab
        driver.close()
        break

# Close the browser window
driver.quit()"""

# import the opencv library
import cv2

# define a video capture object
"""vid = cv2.VideoCapture(0)

while (True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()


"""
"""
import pyttsx3
import speech_recognition as sr
import threading
engine = pyttsx3.init()
r = sr.Recognizer()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(text):
    speak_flag = True
    while speak_flag:

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            print("Say stop to pause the speech or start to resume.")
            audio = r.listen(source)
            try:
                command = r.recognize_google(audio)
                print("You said:______________________________________________________ " + command)
                if "stop" in command:
                    engine.stop()
                    speak_flag = False
                elif "start" in command:
                    engine.stop()
                    speak_flag = True
                    engine.say(text)
                    engine.runAndWait()
            except:
                print("Sorry, I didn't catch that.")

"""