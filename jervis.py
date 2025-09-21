import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import requests
import json
import socket

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def get_weather(city):
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    if response.get("cod") != 200:
        speak(f"Sorry, I could not find weather info for {city}")
        return
    temp = response["main"]["temp"]
    desc = response["weather"][0]["description"]
    speak(f"The current temperature in {city} is {temp} degree Celsius with {desc}")
    print(f"{city}: {temp}°C, {desc}")

def get_news():
    api_key = "YOUR_NEWSAPI_KEY"
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"
    try:
        response = requests.get(url).json()
        articles = response["articles"][:5]
        speak("Here are the top headlines for today")
        for i, article in enumerate(articles, start=1):
            print(f"{i}. {article['title']}")
            speak(f"{i}. {article['title']}")
    except Exception:
        speak("Sorry, I am unable to fetch news right now.")

def take_note():
    speak("What should I write in your note?")
    note = takeCommand()
    if note != "None":
        with open("notes.txt", "a") as f:
            f.write(f"{datetime.datetime.now()}: {note}\n")
        speak("Note saved successfully!")

def show_notes():
    try:
        with open("notes.txt", "r") as f:
            notes = f.read()
        print(notes)
        speak("Here are your notes")
    except FileNotFoundError:
        speak("You have no notes yet.")

def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    speak(f"Your IP address is {ip_address}")
    print(f"IP Address: {ip_address}")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")
        elif 'weather' in query:
            speak("Please tell me the city name")
            city = takeCommand()
            if city != "None":
                get_weather(city)
        elif 'news' in query:
            get_news()
        elif 'take a note' in query:
            take_note()
        elif 'show my notes' in query:
            show_notes()
        elif 'ip address' in query:
            get_ip()
        elif 'shutdown' in query:
            speak("Shutting down your PC in 5 seconds. Goodbye!")
            os.system("shutdown /s /t 5")
        elif 'restart' in query:
            speak("Restarting your PC in 5 seconds.")
            os.system("shutdown /r /t 5")
        else:
            print("No query matched")
