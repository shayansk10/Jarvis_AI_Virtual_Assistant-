# JARVIS Voice Assistant 🎙️

A Python-based voice-controlled personal assistant inspired by JARVIS from Iron Man. This project demonstrates speech recognition, text-to-speech conversion, and automated task execution through voice commands.

## Features
- 🎤 **Voice Recognition** - Speech-to-text conversion using Google's API
- 🔊 **Text-to-Speech** - Responsive voice feedback system
- 🌐 **Web Automation** - Open websites with voice commands
- 🎵 **Music Control** - Play songs from integrated music library
- ⚡ **Wake Word Detection** - Activates with "Jarvis" trigger word
- 🔄 **Real-time Processing** - Continuous listening mode

## Installation & Setup

### Prerequisites
- Python 3.6 or higher
- Microphone hardware
- Internet connection (for speech recognition)

### Required Libraries
pip install speechrecognition pyttsx3 pywin32

## Usage Examples
### Basic Commands
- "Jarvis" → "Ya" → "open google"  # Opens Google
- "Jarvis" → "Ya" → "open youtube" # Opens YouTube
- "Jarvis" → "Ya" → "play believer" # Plays song from library

### Supported Commands
- open google - Opens Google homepage
- open youtube - Opens YouTube
- open linkedin - Opens LinkedIn
- play [song name] - Plays specified song from music library

## Project Structure
### Core Components
- speech_recognition - Audio input and speech-to-text conversion
- pyttsx3 - Text-to-speech engine for voice responses
- webbrowser - Web automation and URL handling
- musicLibrary - Custom music database integration

### Key Functions
- speak(text) - Converts text to speech output
- processCommand(command) - Processes and executes voice commands
- Wake word detection system with "Jarvis" trigger

## Music Library Setup
Create a musicLibrary.py file with your music database:
music = {
    "believer": "https://youtube.com/watch?v=...",
    "shapeofyou": "https://youtube.com/watch?v=...",
    "despacito": "https://youtube.com/watch?v=..."
}

## Technologies Used
- Python 3.x - Core programming language
- SpeechRecognition - Audio processing and STT
- pyttsx3 - Text-to-speech conversion
- Webbrowser - Automated web navigation
- Google Speech API - Cloud-based speech recognition

## Learning Outcomes
- Speech recognition and processing
- Voice command parsing and execution
- Text-to-speech implementation
- Web automation with Python
- Exception handling in audio processing
- Real-time system development

## Future Enhancements
- Add weather information functionality
- Integrate calendar and scheduling
- Implement email reading capabilities
- Add news briefing feature
- Support for multiple languages
- GUI interface for better visualization

## Note
This project requires an active internet connection for speech recognition functionality and may have latency depending on network speed.

