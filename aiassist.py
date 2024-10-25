#voice assiatant
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-in')
        print(f"User said: {command}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return None
    return command.lower()

def main():
    speak("How can I assist you today?")
    while True:
        command = take_command()
        if command is None:
            continue

        if 'hello' in command:
            speak("Hello! How can I help you?")
        elif 'time' in command:
            now = datetime.datetime.now().strftime("%H:%M")
            speak(f"The current time is {now}")
        elif 'date' in command:
            today = datetime.date.today().strftime("%B %d, %Y")
            speak(f"Today's date is {today}")
        elif 'search' in command:
            speak("What do you want to search for?")
            query = take_command()
            if query:
                webbrowser.open(f"https://www.google.com/search?q={query}")
                speak(f"Here are the search results for {query}")
        elif 'exit' in command:
            speak("Goodbye")
            break

if __name__ == "__main__":
    main()
