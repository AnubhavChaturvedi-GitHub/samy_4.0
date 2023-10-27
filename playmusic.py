import pywhatkit as kit
from speak import speak
from listen import listen

def play_music_on_youtube(song_name):
    try:
        kit.playonyt(song_name)
        speak(f"Playing '{song_name}' on YouTube...")
    except Exception as e:
        speak(f"An error occurred: {str(e)}")

