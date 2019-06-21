import speech_recognition as sr
import os
from playsound import playsound
import webbrowser
import random

speech = sr.Recognizer
greeting_dict = {"hello":"hello","hi":"hi"}

def play_sound(mp3_list):
        mp3 = random.choice(mp3_list)
        playsound(mp3)

def read_voice_cmd():
    voice_text = ""
    print("Listening")
    with sr.Microphone() as source:
        audio = speech.listen(source)
        audio = speech.listen(source=source, timeout=10,phrase_time_limit=5)

    try:
        voice_text = speech.recognize_google(audio)
    except sr.UnkownValueError:
        pass
    except sr.RequestError as e:
        print("Network Error")
    except sr.WaitTheTimeOut:
        pass
    return voice_text


if __name__ == "__main__":

    playsound("")

    while True:

        voice_note = read_voice_cmd()
        print("cmd : {}".format(voice_note))

        if 'hello' in voice_note:
            continue
        elif "open" in voice_note:
            os.system('explorer C:\\"{}"'.format(voice_note.replace("open ", "")))
            continue
        elif "by" in voice_note:
            exit()
