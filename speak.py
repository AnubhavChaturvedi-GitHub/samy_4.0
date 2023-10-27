import pyttsx3
import threading

def speak(text):
    def speak_thread(text):
        engine = pyttsx3.init()
        
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[2].id)
        engine.setProperty('rate', 170)
        engine.say(text)
        engine.runAndWait()

    speak_thread = threading.Thread(target=speak_thread, args=(text,))
    speak_thread.start()
    speak_thread.join()
