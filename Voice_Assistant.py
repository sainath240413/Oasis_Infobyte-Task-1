import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    """Recognize voice input using microphone."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I didn't understand.")
            return ""
        except sr.RequestError:
            print("Network error.")
            return ""

def respond(command):
    """Process user commands."""
    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")
    elif "date" in command:
        today_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {today_date}")
    elif "search" in command:
        query = command.replace("search", "").strip()
        speak(f"Searching for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")
    else:
        speak("I'm sorry, I can't do that yet.")

if __name__ == "__main__":
    speak("Hello! I am your voice assistant.")
    while True:
        user_command = recognize_speech()
        if "exit" in user_command or "stop" in user_command:
            speak("Goodbye!")
            break
        respond(user_command)
