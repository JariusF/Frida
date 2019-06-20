import speech_recognition as sr
import pyttsx3

speech = sr.Recognizer

try:
    engine = pyttsx3.init()
except ImportError:
    print("Requested driver is not Found")
except RuntimeError:
    print("Driver failed to initialize")

voices = engine.getProperty('voices')

for voice in voices:
    print("voice, voice.id")
engine.setProperty("voice", voice.id)
engine.say("Hello Sir. This is friday")
engine.runAndWait()

def speack_text_cmd(cmd):
    engine.say(cmd)
    engine.runAndWait()

def read_voice_command():
    voice_text = ""
    with sr.Microphone() as source:
       audio = speech.listen(source)
    try:
       voice_text = speech.recognize_google(audio)
    except sr.UnkownValueError:
        pass
    except sr.RequestError as e:
        print("Network Error")
    return voice_text



if __name__ == "__main__ ":

    speak_text_cmd("Hello Small Black Star, This is Friday")

    while True:

        voice_note = read_voice_cmd()

        if "hello" in voice_note:
            speak_text_cmd("")






