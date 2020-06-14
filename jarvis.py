import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
Master = "raahul sir"
print("Initializing p.r.i.y.a")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():

    hour = int(datetime.datetime.now().hour)
    
    if 0<=hour<12:
        speak("good morning"+ Master)

    elif 12<hour<18:
        speak("good afternoon"+ Master)   

    else:
        speak("good evening"+ Master)

    speak(" i am priya sir please tell me how can i assist you ")    

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listining....")
        r.pause_threshold=1
        audio = r.listen(source)
        
    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language= 'en-in' )
        print(f"user said: {query}\n ")

    except Exception as e :
        print("say that again please")
        query= None
    return query   
#main starts here

if __name__ == "__main__":
    speak("Initializing priya")
    con = 1
    wishMe()
    while con!=2:
        query = takeCommand().lower()
        if 'wikipedia' in  query:
            speak("searching wikipedia......rahul sir")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences  =2)
            speak(results)
        elif 'open youtube' in query:
            url = "youtube.com"
            speak("oppening youtube rahul sir")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open google' in query:
            speak("opening google rahul sir")
            url = "google.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open stackoverflow' in query:
            speak("opening stackoverflow rahul sir")
            url = "stackoverflow.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open reddit' in query:
            speak("oppenning reddit rahul sir")
            url = "reddit.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open notepad' in query:
           path = "C:\\Users\\jeevan kumar\\AppData\Roaming\\Microsoft\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
           speak("reddit")
           os.startfile(path)

        elif 'play music' in  query:
            speak("playing rahul sir")
            song_dict = "C:\\Users\jeevan kumar\\OneDrive\\Desktop\\jarvis songs"
            songs = os.listdir(song_dict)
            print(songs)  
            speak("which index song you want to play")
            song=int(takeCommand())
            #if song in songs:
            os.startfile(os.path.join(song_dict, songs[song]))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"rahul sir, the time is {strTime}")

            
        elif 'open my project' in query:
            path = "C:\\Users\\jeevan kumar\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(path)


        elif 'thanks priya' in query:
            con =int(con) + 1
            speak("your welcome baava")

        elif 'love you priya' in query:
            con =int(con)  + 1
            speak("love you to rahul baava") 

        elif 'open face book' in query:
            speak("opening face book rahul sir")
            url = "facebook.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
           
             

        elif 'open instagram' in query:
            speak("opening instagram")
            url = "instagram.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

            
        elif 'open watsapp' in query:
            speak("opening whatsapp   rahul sir")
            path ='C:\\Users\\jeevan kumar\\AppData\\Local\\WhatsApp'
            os.startfile(path)
           
        
        elif 'my photos' in query:
            speak("opening my photos rahul sir")
            path ='C:\\Users\\jeevan kumar\\OneDrive\\Desktop\\my photos'
            os.startfile(path)   