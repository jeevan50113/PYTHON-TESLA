#imprt statements
import datetime
import smtplib
import tkinter as tk
import webbrowser
import os
import time as t
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pyttsx3  # pip install pyttsx3
import pywhatkit as kit
import speech_recognition as sr  # pip install speechRecognition
import weather_forecast as wf

# setting of global variables
listining_engine = pyttsx3.init('sapi5')
speaking_voices = listining_engine.getProperty('voices')  # print(voices[1].id)
listining_engine.setProperty('voice', speaking_voices[0].id)
win = None
e1 = None
e2 = None
e3 = None
b = None


# functions
# speack function which takes text input and speaks it
def speak(audio):
    listining_engine.say(audio)
    listining_engine.runAndWait()


# depending upon time it wishes mw
def wishMe():
    time = int(datetime.datetime.now().hour)
    if 0 <= time < 12:
        speak("Good Morning!")

    elif 12 <= time < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am lalith Sir. Please tell me how may I help you")


# It takes microphone input from the user and calls process function
def takeCommand():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        rec.pause_threshold = 1
        audio = rec.listen(source)

    try:
        print("Recognizing...")
        query = rec.recognize_google(audio, language='en-in')
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    process(query)


def send_mail():
    #https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4PY4_lBCtDFFqgYXrId0u7bKf7JtI-J6sTVKkz41sCeCMfWt-7ayR17_e2fdrjDgArUlYTOLlNfELeFHPOXdkNeI2wk9g
    #go to above site and allow less secure apps
    fromaddr = "gullanianirudh1000@gmail.com"
    toaddr = e1.get()
    bod= e2.get()
    fil = e3.get()
    e1.pack_forget()
    e2.pack_forget()
    e3.pack_forget()
    b.pack_forget()
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Subject of the Mail"
    body = bod
    msg.attach(MIMEText(body, 'plain'))
    if(fil!=''):
        filename = fil
        attachment = open(filename, "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, "enter your password")
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()


def open_file():
    filename = e1.get()
    path_wanted = None
    dir_path = os.path.dirname(os.path.realpath(__file__))
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file == filename:
                path_wanted = root + '\\' + str(file)
    if path_wanted == None:
        dir_path = os.path.dirname("D:\\")
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file == filename:
                    path_wanted = root + '\\' + str(file)
    if path_wanted == None:
        dir_path = os.path.dirname("E:\\")
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file == filename:
                    path_wanted = root + '\\' + str(file)
    os.startfile(path_wanted)
    e1.pack_forget()
    b.pack_forget()


def weather():
    place = e1.get()
    now = datetime.datetime.now()
    date = now.strftime("%y%y-%m-%d")
    time = (now.strftime("%H:%M:%S"))
    fore=(wf.forecast(place=place, time=time, date=date, forecast="daily"))
    print(fore)
    speak(fore)
    e1.pack_forget()
    b.pack_forget()


def process(query):
    query1 = query.split(' ')
    print(f"User said: {query}\n")

    # speak(query)

    if ('open' in query1) and ('file' in query1):
        b["command"] = open_file
        e1.pack()
        b.pack()
        speak('enter file name')


    elif 'exit' in query1:
        speak(" Thank you sir have a nice day ")
        print("Thank you sir have nice day")
        exit()

    elif ('mail' in query1) or ('email' in query1):
        b["command"] = send_mail
        print("sending... email")
        e1.pack()
        e2.pack()
        e3.pack()
        b.pack()
        speak("fill details")


    elif (('open' in query1) and ('youtube' in query1)) or ('youtube' in query1) or ('YouTube' in query1):
        speak("opening youtube")
        print("opening youtube")
        searc_query = query.replace("youtube", ' ').replace('open', ' ').replace('in', ' ')
        webbrowser.open('https://youtube.com/results?search_query=' + searc_query)


    elif ('weather' in query1) or ('forecast' in query1):
        b["command"] = weather
        speak("enter the place")
        e1.pack()
        b.pack()

    elif ("time" in query1) or ("date" in query1):

        now = datetime.datetime.now()
        date = now.strftime("%y%y-%m-%d")
        time = now.strftime("%H:%M")
        print("time is" + time + "and date is" + date)
        speak("time is" + time.replace(':',' ') + "and date is" + date.replace('-',' '))


    elif "none" in query:
        print("sir you have being silent can i exit sir")
        speak("sir you have being slient can i exit sir")


    elif ('do' in query1) or ('can' in query1) :
        print("1.i can open files for you\n 2.i can play your wised youtube video\n"
              "3.i can help you to know about wheather forecast\n"
              "4. i can tell you the time and date\n"
              "5.i can browse the information for you\n"
              "6.i can send email for you"
              "\n7.i can self exit my self for you")
        speak("i can open files for you i can play your wised youtube video"
              " i can help you to know about wheather forecast"
              "i can tell you the time and date i can browse the information for you  i can send email for you"
              "last but not least i can self exit my self for you")

    elif ("result google" in query1) or ("search google" in query1):
        kit.search(query)


    else:

        try:
            speak('Searching google')
            kit.search(query)
        except Exception:
            speak('no such results found')


def Fun(fun):
    print('nothing')


if __name__ == "__main__":
    win = tk.Tk()
    win.geometry("500x250+1200+650")
    win.title("JARVIS")
    tk.Button(win, text="Give command", width=14, command=takeCommand).pack()
    e1 = tk.Entry(win)
    e2 = tk.Entry(win)
    e3 = tk.Entry(win)
    b = tk.Button(win, text='ok', width=6, command=Fun)
    win.mainloop()
