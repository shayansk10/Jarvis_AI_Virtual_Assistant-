import speech_recognition as sr
import pyttsx3
import webbrowser
import time
import musicLibrary  

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif "play" in c:
        parts = c.split()
        if len(parts) > 1:
            song = parts[1]
            link = musicLibrary.music.get(song)
            if link:
                webbrowser.open(link)
            print(f"Would play: {song}")

if __name__=="__main__":
    speak("Initializing Jarvis.")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=2)
            word = recognizer.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("Ya")
                time.sleep(1)  

                with sr.Microphone() as source:
                    print("Jarvis is now active!")
                    audio = recognizer.listen(source, timeout=3)
                    command = recognizer.recognize_google(audio)

                    if command:
                        processCommand(command)
                    else:
                        print("No command detected.")

        except Exception as e:
            print("Error; {0}".format(e))
