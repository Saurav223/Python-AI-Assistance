import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init()
engine.setProperty('rate',160)
engine.setProperty('volume',1)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <=12:
        speak("Good Morning sir!")

    elif hour >= 12 and hour <=18:
        speak("Good Afternoon sir!")

    else:
        speak("Good Evening sir!")

    speak("I am your assistance. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 100
        audio = r.listen(source)

    try:
        print("Recognizer")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
        return query

    except Exception as e:
      #  print(e)
        print('Say that again please....')
        return 'None'
    
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your-password')
    server.sendmail('youremail',to,content)

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            musicdir ='D:\YMusic'
            if os.path.exists(musicdir):
                files = os.listdir(musicdir)
                songs = []
                for file in files:
                    if file.endswith('.mp3'):
                        songs.append(file)
           # print(songs)
                if songs:
                    ran = random.randint(0,len(songs)-1)
                    os.startfile(os.path.join(musicdir, songs[ran]))
                else:
                    speak('No music files found in the directory')
            else:
                speak('Music directory not found')
                

        elif 'time' and 'now' in query:
            hour = datetime.datetime.now().hour
            min = datetime.datetime.now().minute
            ap = ''
            if hour > 12:
                hour = hour - 12
                ap = 'pm'
            else:
                ap = 'am'
            speak(f'Its {hour} {min} {ap}')

        elif 'open' and 'code' in query:
            codepath = 'C:\\Users\\Acer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codepath)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'subedis440@gmail.com'
                sendEmail(to,content)
                speak("Email has been sent!")

            except Exception as e:
                speak("Sorry I am not able to send this email !")

