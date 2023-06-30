import speech_recognition as sr
import pyttsx3
import threading
import pyttsx3
import pyttsx3

from google.cloud import texttospeech
import pyttsx3

# Set up Google Cloud Text-to-Speech client
client = texttospeech.TextToSpeechClient()

# Set the voice (choose a voice from the available options)
voice = texttospeech.VoiceSelectionParams(
    language_code='en-US',
    ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
    name='en-US-Wavenet-D'
)

# Set the audio format
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Convert text to speech using Google Cloud Text-to-Speech
text = "Hello, how are you?"
input_text = texttospeech.SynthesisInput(text=text)
response = client.synthesize_speech(input=input_text, voice=voice, audio_config=audio_config)

# Save the synthesized speech as an MP3 file
output_file = 'output.mp3'
with open(output_file, 'wb') as out:
    out.write(response.audio_content)

# Play the synthesized speech using pyttsx3
engine.setProperty('voice', output_file)
engine.say(text)
engine.runAndWait()





"""
def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source , duration=1)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return None

def listen_thread():
    global paused
    while True:
        if not paused:
            command = listen()
            if command:
                if 'stop' in command.lower():
                    paused = True
                    speak("Speech paused.")
                elif 'resume' in command.lower():
                    paused = False
                    speak("Speech resumed.")
                elif 'exit' in command.lower():
                    speak("Goodbye!")
                    break

speak("Hello, I am ready to speak. Say 'stop' to pause or 'resume' to continue.")

paused = False
thread = threading.Thread(target=listen_thread)
thread.start()

while True:
    if not paused:
        speak("What would you like me to say?")
        text = input("Enter text to speak: ")
        if text:
            speak(text)
    else:
        speak("Speech is paused. Say 'resume' to continue.")
        command = input("Enter command: ")
        if 'resume' in command.lower():
            paused = False
"""