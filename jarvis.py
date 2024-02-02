import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")   
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
        speak("good evening!")
        
    speak("I am doraemon, please tell me how may i help ou today")
    
def takeCommand():
    # It takes microphone input from the user and returns string output
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said: {query}\n")
        
    except Exception as e:
        # Uncomment this line if you want to print the exception
        # print(e)
        
        print("Sorry, I couldn't understand that. Please say that again.")
        return "None"
    return query

def sendEmail(to,content):
   server = smtplib.SMTP('smtp.gmail.com', 587)
   server.ehlo()
   server.starttls()
   server.login('akshatasnippani99@gmail.com','Ak@123456')
   server.sendmail('youremail@gmail.com',to,content)
   server.close()
   
if __name__ == "__main__":
    wishme()
    if 1:
        query = takeCommand().lower()

        # logic for executing tasks on query
        if 'wikipedia' in query:
            speak('Searching wikipedia')
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open chatgpt' in query:
            webbrowser.open("chatgpt.com")
        elif 'play music' in query:
            music_dir = "C:\\Users\\Akshata S\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime =  datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"hello ma'am, The time is {strTime}")
        elif 'open code' in query:
              codepath= "C:\\Users\\Akshata S\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"  
              os.startfile(codepath)
        elif 'email to akshata' in query:   
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "akshatas229@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry, my frnd i am not able to send the this email at this moment")