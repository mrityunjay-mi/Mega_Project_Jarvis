import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

# pip install pocketsphinx

recognizer = sr.Recognizer()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open asurascans" in c.lower():
        webbrowser.open("https://asurascans.com")
    elif "youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link) 

if __name__ == "__main__":
    speak("Initializing jarvis.....")
    while True:
        # Listen to the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=2 , phrase_time_limit= 1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes master")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

    
        except Exception as e:
            print("Error; {0}".format(e))