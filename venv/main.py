import os
import datetime
import playsound
import speech_recognition as sr
from gtts import gTTS
import wikipedia



def speak(text):
    os.remove("voice.mp3")
    tts = gTTS(text=text, lang="en-in")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def get_audio():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            print("Recognizing...")
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception : "+str(e))

    return said


speak("How Can I Help You Sir?")

print("Listening....")

text = get_audio()

if "Wikipedia" in text:
    speak("Searching Wikipedia")
    query = text.replace("Wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia " +results)

if "the time" in text:
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak("Sir, The Time is : "+strTime)



if "what is your name" in text:
    speak("I am the Hilarious")

