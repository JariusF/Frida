import speech_recognition as sr
import pyttsx3
import os


try:
    engine = pyttsx3.init()
except ImportError:
    print("Requested driver is not Found")
except RuntimeError:
    print("Driver failed to initialize")

voices = engine.getProperty('voices')

for voice in voices:
    engine.setProperty("voice", " HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')")
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



if __name__ == "__main__":

    while True:

        voice_note = read_voice_cmd()
        print("cmd : {}".format(voice_note))

        if 'hello' in voice_note:
            continue
        elif "open" in voice_note:
            speak_text_cmd("ok sir.")
            os.system('explorer C:\\"{}"'.format(voice_note.replace("open ", "")))
            continue
        elif "by" in voice_note:
            speak_text_cmd("By Star, Happy to help you. Have a good day!")
            exit()







