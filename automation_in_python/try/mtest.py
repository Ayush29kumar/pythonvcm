import threading
import speech_recognition as sr
import time

# create a global recognizer object
r = sr.Recognizer()

# define a function to read audio from microphone
def read_microphone():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        while True:
            audio = r.listen(source)
            recognize_speech(audio)

# define a function to recognize speech from audio
def recognize_speech(audio):
    try:
        text = r.recognize_google(audio)
        print("You said: {}".format(text))
        # update the text box here with the recognized text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# create a thread to read audio from microphone
microphone_thread = threading.Thread(target=read_microphone)

# start the microphone thread
microphone_thread.start()
# wait for the microphone thread to finish
microphone_thread.join()
