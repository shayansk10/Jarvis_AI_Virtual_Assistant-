import speech_recognition as sr
import pyttsx3
import time
import os
import tempfile
import   # pip install pygame

# Initialize TTS engine
engine = pyttsx3.init('sapi5')  # Windows, use 'nsss' for Mac
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('volume', 1.0)

recognizer = sr.Recognizer()

# Speak function using temporary mp3 file and pygame
def speak(text):
    # Create temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        temp_file = f.name
    engine.save_to_file(text, temp_file)
    engine.runAndWait()

    # Play the audio using pygame
    pygame.mixer.init()
    pygame.mixer.music.load(temp_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    os.remove(temp_file)

# Listen function
def listen_command(timeout=5):
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source, timeout=timeout)
    try:
        command = recognizer.recognize_google(audio)
        return command.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""

# Process command
def process_command(command):
    print("Command received:", command)

# Main Jarvis loop
if __name__ == "__main__":
    speak("Initializing Jarvis")
    time.sleep(0.5)

    while True:
        command = listen_command(timeout=3)

        if "jarvis" in command:
            speak("Ya")  # now guaranteed to play
            time.sleep(0.5)  # short pause

            # Listen for actual command
            command = listen_command(timeout=5)
            if command:
                process_command(command)
            else:
                print("No command detected.")
