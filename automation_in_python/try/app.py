"""import speech_to_text

# Create a client object.
client = speech_to_text.SpeechToTextClient()

# Start listening for audio.
stream = client.start_streaming(
    microphone=True,
    language_code='en-US'
)

# Transcribe the audio as it is being recorded.
while True:
    result = stream.read()
    if result.error:
        print(result.error)
        break
    print(result.alternatives[0].transcript)"""
"""from google.cloud import texttospeech

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text="Hello, world!")

# Build the voice request
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')"""
import speech_recognition as sr
import tkinter as tk

# Create a speech recognition object
r = sr.Recognizer()

# Create a GUI window with a textbox
window = tk.Tk()
textbox = tk.Text(window, height=10, width=50)
textbox.pack()

# Define a function to continuously transcribe speech and update the textbox
def transcribe_speech():
    # Use the microphone as the audio source
    with sr.Microphone() as source:
        # Adjust for ambient noise
        r.adjust_for_ambient_noise(source)
        # Continuously listen for speech and transcribe it
        x = 0
        while True:
            try:
                audio = r.listen(source)
                text = r.recognize_google(audio, language='en-US')
                # Write the transcribed text into the textbox
                textbox.insert(tk.END, text + " ")
                # Scroll to the end of the textbox to show the latest text
                textbox.see(tk.END)
            except sr.UnknownValueError:
                print(sr.UnknownValueError)
                print("Speech recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from speech recognition service; {0}".format(e))

# Add a button to start transcribing speech
button = tk.Button(window, text="Transcribe Speech", command=transcribe_speech)
button.pack()

window.mainloop()

