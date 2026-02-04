import speech_recognition as sr
import pyttsx3
import requests
import datetime
import cv2
import threading
import time
WEATHER_API_KEY = "YOUR_OPENWEATHER_API_KEY"
NEWS_API_KEY = "YOUR_NEWS_API_KEY"
CITY = "Delhi"
engine = pyttsx3.init()
recognizer = sr.Recognizer()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio).lower()
    except:
        return ""
def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={WEATHER_API_KEY}&units=metric"
    data = requests.get(url).json()
    speak(f"Temperature is {data['main']['temp']} degree Celsius")
def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"
    data = requests.get(url).json()
    for article in data['articles'][:5]:
        speak(article['title'])
def set_reminder(seconds, message):
    time.sleep(seconds)
    speak("Reminder: " + message)
def video_mode():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow("Assistant", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
def assistant():
    speak("Hello, I am your personal assistant")
    while True:
        command = listen()
        if "weather" in command:
            get_weather()
        elif "news" in command:
            get_news()
        elif "reminder" in command:
            speak("Tell seconds")
            seconds = int(listen())
            speak("Message")
            msg = listen()
            threading.Thread(target=set_reminder, args=(seconds, msg)).start()
        elif "video" in command:
            video_mode()
        elif "exit" in command:
            speak("Goodbye")
            break
assistant()