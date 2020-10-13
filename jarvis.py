import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
Master = "jeevan sir"
print("preparing T.E.S.L")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
#
def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():

    hour = int(datetime.datetime.now().hour)
    
    if 0<=hour<12:
        speak("happy morning"+ Master)

    elif 12<hour<18:
        speak("happy afternoon"+ Master)   

    else:
        speak("happy evening"+ Master)

    speak(" this tesla how can i help you ")    

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
#main s

if __name__ == "__main__":
    speak("preparing tesla")
    con = 1
    wishMe()
    while con!=2:

        query = takeCommand().lower()

        if 'wikipedia' in  query:
            speak("searching wikipedia......sir")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences  =2)
            speak(results)
        elif 'open youtube' in query:
            url = "youtube.com"
            speak("oppening youtube ")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open google' in query:
            speak("opening google ")
            url = "google.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)
            
        elif 'open stack overflow' in query:
            speak("opening stackoverflow ")
            url = "stackoverflow.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open reddit' in query:
            speak("oppenning reddit")
            url = "reddit.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open notepad' in query:
           path = "C:\\Users\\jeevan kumar\\AppData\Roaming\\Microsoft\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
           speak("reddit")
           os.startfile(path)

        elif 'play music' in  query:
            speak("playing  sir")
            song_dict = "C:\\Users\\jeevan kumar\\OneDrive\\Desktop\\jarvis\\jarvis songs"
            songs = os.listdir(song_dict)
            print(songs)  
            
            #speak("which index song you want to play")
            #song=int(takeCommand())
            #if song in songs:
            os.startfile(os.path.join(song_dict, songs[0]))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"sir, the time is {strTime}")
            
           #you should give you folder path to open you project 
        elif 'open my project' in query:
            path = "C:\\Users\\jeevan kumar\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(path)


        elif 'thanks telsa' in query:
            con =int(con) + 1
            speak("your welcome sir")

      
       #in this bit facebook will not open in chrome it will open in default webbrowser i.e internet explorer 
        elif 'open facebook' in query:
            speak("opening face book ")
           # url= "facebook.com"
            #chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.ex'
            webbrowser.open("facebookcom")
           
             
       
       #in this bit facebook will not open in chrome it will open in default webbrowser i.e internet explorer 
        elif 'open instagram' in query:
            speak("opening instagram")
            # url e %s= "facebook.com"
            #chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.ex'
            webbrowser.open("instagram.com")

            
        elif 'open WatsApp' in query:
            speak("opening whatsapp ")
            path ='C:\\Users\\jeevan kumar\\AppData\\Local\\WhatsApp'
            os.startfile(path)
           
        #you should give you folder path to open phontos
        #the path specified in the code is my folder path so just remove it and add yours
        elif 'my photos' in query:
            speak("opening my photos ")
            path ='C:\\Users\\jeevan kumar\\OneDrive\\Desktop\\my photos'
            os.startfile(path)   
