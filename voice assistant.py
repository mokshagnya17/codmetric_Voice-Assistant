import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import pyautogui
from plyer import notification
from bs4 import BeautifulSoup
import requests
from gtts import gTTS
#from news import speak_news, getNewsUrl
#from OCR import OCR
#from diction import translate
from helpers import *
#from youtube import youtube
from sys import platform
from pprint import pprint
from selenium import webdriver
import os
import getpass

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello boss. Please tell me how may I help you") 
def make_request(url):
  response = requests.get(url)
  return response.text      


def lighton():
    driver = webdriver.Chrome('C:/Users/Username/Downloads/chromedriver.exe')#add the location of the chrome Drivers
    driver.get("https://Add here.000webhostapp.com/main.html")#Add the webhost name
    elem1 = driver.find_element_by_id("S1off")
    elem1.click()

def lightoff():
    driver = webdriver.Chrome('C:/Users/manbirmarwah/Downloads/chromedriver.exe')
    driver.get("https://Add here.000webhostapp.com/main.html")#Add the webhost name
    elem1 = driver.find_element_by_id("S1on")
    elem1.click()
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

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mokshagnyapilli@gmail.com', 'your-password')
    server.sendmail('mokshagnyapilli@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'are you' in query:
            speak("I am joodo developed by Aditya prakash")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'screenshot' in query:
            image = pyautogui.screenshot()
            image.save('screenshot.png')
            speak('Screenshot taken.')
        elif 'open search tab' in query:
            speak("What do you want me to search for (please type) ? ")
            search_term = input()
            search_url = f"https://www.google.com/search?q={search_term}"
            webbrowser.get(
            'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(search_url)
            speak(f"here are the results for the search term: {search_term}")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
        elif 'shutdown' in query:
            if platform == "win32":
                os.system('shutdown /p /f')
        elif platform == "linux" or platform == "linux2" or "darwin":
                os.system('poweroff')
        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            webbrowser.open("web.whatsapp.com")
        elif 'play music' in query:
            music_dir = 'D:\\testproject\\songs\\Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'local disk d' in query:
            speak("opening local disk D")
            webbrowser.open("D://")
        elif 'local disk c' in query:
            speak("opening local disk C")
            webbrowser.open("C://")
        elif 'local disk e' in query:
            speak("opening local disk E")
            webbrowser.open("E://")
            
        elif 'single' in query:
            speak('I am in a relationship with wifi')
        elif 'joke' in query:
            speak(pyjokes.get_joke())
            speak('Thanks sir')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif "where i" in query:
           query = query.split(" ")
           location = query[2]
           speak("Hold on Mokshagnya, I will show you where " + location + " is.")
           os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")

        elif 'remember that' in query:
            speak("what should i remember sir")
            rememberMessage = takeCommand()
            speak("you said me to remember"+rememberMessage)
            remember = open('data.txt', 'w')
            remember.write(rememberMessage)
            remember.close()
            """
        elif 'dictionary' in query:
            speak('What you want to search in your intelligent dictionary?')
            translate(takeCommand())
             elif 'voice' in query:"""
        elif 'female' in query:
                engine.setProperty('voice', voices[0].id)
        elif 'male' in query:
                engine.setProperty('voice', voices[1].id)
                speak("Hello Sir, I have switched my voice. How is it?")
        elif 'do you remember anything' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that" + remember.read())
            """elif 'news' in query:
            speak('Ofcourse sir..')
            speak_news()
            speak('Do you want to read the full news...')
            test = takeCommand()
            if 'yes' in test:
                speak('Ok Sir, Opening browser...')
                webbrowser.open(getNewsUrl())
                speak('You can now read the full news from this website.')
            else:
                speak('No Problem Sir')"""
        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'covid stats' in query:
            html_data = make_request('https://www.worldometers.info/coronavirus/')
         # print(html_data)
            soup = BeautifulSoup(html_data, 'html.parser')
            total_global_row = soup.find_all('tr', {'class': 'total_row'})[-1]
            total_cases = total_global_row.find_all('td')[2].get_text()
            new_cases = total_global_row.find_all('td')[3].get_text()
            total_recovered = total_global_row.find_all('td')[6].get_text()
            print('total cases : ', total_cases)
            print('new cases', new_cases[1:])
            print('total recovered', total_recovered)
            notification_message = f" Total cases : {total_cases}\n New cases : {new_cases[1:]}\n Total Recovered : {total_recovered}\n"
            notification.notify(
            title="COVID-19 Statistics",
            message=notification_message,
            timeout=5
                    )
        
            speak("here are the stats for COVID-19")
        elif 'turn on lights' in query:
            speak("Turning on the lights.")
            lighton()
            speak("Lights are on")
        
        elif 'turn off lights' in query:
            speak("OK,sir turning off the Lights")
            lightoff()
            speak("Lights are off")   
        elif 'how is the weather' and 'weather' in query:

            url = 'https://api.openweathermap.org/'#Open api link here

            res = requests.get(url)

            data = res.json()

            weather = data['weather'] [0] ['main'] 
            temp = data['main']['temp']
            wind_speed = data['wind']['speed']

            latitude = data['coord']['lat']
            longitude = data['coord']['lon']

            description = data['weather'][0]['description']
            speak('Temperature : {} degree celcius'.format(temp))
            print('Wind Speed : {} m/s'.format(wind_speed))
            print('Latitude : {}'.format(latitude))
            print('Longitude : {}'.format(longitude))
            print('Description : {}'.format(description))
            print('weather is: {} '.format(weather))
            speak('weather is : {} '.format(weather))
 
        
        elif 'it\'s my birthday today' in query:
            print(" Wow! Wish you a very Happy Birthday")
            speak(" Wow! Wish you a very Happy Birthday")
        elif 'email to Mokshagnya' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "pillimokshagnya1026@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")        