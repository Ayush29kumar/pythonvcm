import speech_recognition as sr
r = sr.Recognizer()
import subprocess
def usemic(a,b):
    while True:
        with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source , duration=1)
                print(b ,a)
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                    text = text.lower()
                    print(f"the text is {text}")
                    return text
                except sr.UnknownValueError:
                    print("Sorry, I could not understand what you said.")
                except sr.RequestError as e:
                    print("Sorry, could not request results from Google Speech Recognition service; {0}".format(e))


def say(text):
    def festival_tts(text):
        command = f'(voice_cmu_us_rms_cg) (SayText "{text}")'
        festival_process = subprocess.Popen(['festival', '--pipe'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

        festival_process.stdin.write(command.encode())
        festival_process.stdin.flush()

        output, _ = festival_process.communicate()

        festival_process.terminate()

        output = output.decode()

        return output
    output = festival_tts(text)
    print(output)

