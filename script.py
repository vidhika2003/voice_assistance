import speech_recognition as sr
import pyttsx3

def listen():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use microphone as input
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-us')
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        print("Sorry, I'm having trouble accessing Google Speech Recognition service.")
        return ""

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    if "weather" in command:
        speak("The weather is sunny today.")
    elif "news" in command:
        speak("Here are the top news headlines.")
    elif "joke" in command:
        speak("Why don't scientists trust atoms? Because they make up everything!")
    elif "stop" in command or "exit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I didn't understand that.")

if __name__ == "__main__":
    speak("Hello, I'm your personal assistant. How can I help you today?")
    while True:
        command = listen()
        process_command(command)