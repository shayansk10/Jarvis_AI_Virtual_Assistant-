import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif "play" in c.lower():
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

if __name__=="__main__":
    speak("Initializing Jarvis.")

    while True:
        r = sr.Recognizer()

        print("Recognizing...") 
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2)       
            word = r.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("Ya")
                
                with sr.Microphone() as source:
                    print("Jarvis is now active!")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
