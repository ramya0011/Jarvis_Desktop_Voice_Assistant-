import cv2
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from requests import get
import pywhatkit as kit
import sys
import pyjokes
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        print("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        print("Good Afternoon!")

    else:
        speak("Good Evening!")
        print("Good Evening!")

    speak("I am Jarves Sir. Please tell me how may I help you")
    print("I am Jarves Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def screenshot():
    img = pyautogui.screenshot()
    img_path = os.path.expanduser("~\\Pictures\\ss.png")
    img.save(img_path)

if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if "who are you" in query:
            speak("I'm JARVES and I'm a desktop voice assistant.")
            print("I'm JARVES and I'm a desktop voice assistant.")

        elif "how are you" in query:
            speak("I'm fine sir, What about you?")
            print("I'm fine sir, What about you?")

        elif "fine" in query:
            speak("Glad to hear that sir!!")
            print("Glad to hear that sir!!")

        elif "good" in query:
            speak("Glad to hear that sir!!")
            print("Glad to hear that sir!!")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Sir, What should I search on Google")
            cm = takeCommand().lower()
            url=f"https://www.google.com/search?q={cm}"
            webbrowser.open(url)

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = 'C:\\Users\\DELL\\Music\\Playlists\\'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\DELL\\Desktop\\sahad-proj"
            os.startfile(codePath)

        elif 'open notepad' in query:
            nPath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(nPath)

        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'open camera' in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret,img=cap.read()
                cv2.imshow('webcam',img)
                if cv2.waitKey(1) & 0xFF==ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "ip address" in query:
            ip=get('https://api.ipify.org/').text
            print(ip)
            speak(f"your IP address is {ip}")

        elif "open facebook" in query:
            webbrowser.open("facebook.com")

        elif "send message" in query:
            speak("what is the message? sir")
            message = takeCommand().lower()
            now=datetime.datetime.now()
            hour=now.hour
            min=now.minute+1
            kit.sendwhatmsg("+919449982165",message,hour,min)

        elif "play song on youtube" in query:
            speak("Sir, What should I play on YouTube")
            yt = takeCommand().lower()
            kit.playonyt(yt)

        elif "tell me a joke" in query:
            joke=pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif "no thanks" in query:
            speak("thanks for using me,sir have a good day")
            sys.exit()

        elif "shut down the system" in query:
            os.system("shutdown /s /t S")

        elif "restart the system" in query:
            os.system("shutdown /r /t S")

        elif "open job portal" in query:
            webbrowser.open("https://www.linkedin.com/home?originalSubdomain=in")

        elif "screenshot" in query:
            screenshot()
            print("I've taken screenshot, please check it")
            speak("I've taken screenshot, please check it")

        else:
            print("No query matched")

        speak("sir,do you have any other work")