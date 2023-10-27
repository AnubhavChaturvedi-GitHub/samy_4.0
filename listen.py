import speech_recognition as sr

# Function to listen for speech
def listen():
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 0.2
    recognizer.non_speaking_duration = 0.2

    with sr.Microphone() as source:
        # Modify the pause_threshold and non_speaking_duration
        recognizer.adjust_for_ambient_noise(source)  # Use the same duration as non_speaking_duration
        print("Listening...")
        audio = recognizer.listen(source,timeout=None)  # No timeout specified
        print("Recognizing...")

    try:
        recognized_text = recognizer.recognize_google(audio)
        print(f"You said: {recognized_text}")
        return recognized_text
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    return ""

