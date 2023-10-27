from listen import listen
from speak import speak
from brain import search_brain
from open_operation import open_youtube
from open_operation import open_chrome
from open_operation import open_insta
from open_operation import open_telegram
from open_operation import open_whatsapp
import webbrowser
import pyautogui as gui
from wish import wish
import threading
from brain import load_qa_data
import time
from playmusic import play_music_on_youtube
from Youtube import NetHyFun_Count
from Youtube import Night_Conspiracy_Count
from Youtube import NetHyToons_Count
from Youtube import Royal_Free_Music_NCS_Count
from open_operation import open_chat_GPT
from openaibrain import chat_with_ai
from brain import wiki_search
from brain import print_animated_message
from brain import save_qa_data

qa_file_path = "C:\\Users\\Anubhav\\OneDrive\\Desktop\\Samy_3.0\\qna_logbook.txt"
qa_dict = load_qa_data(qa_file_path)

def main():
    wish()
    while True:
        text = listen().lower()

        if text.startswith(("who is ", "what is ", "how to ","what are"," show me", "tell me", "tell me about")):
            search_brain(text)
            continue


        elif "open youtube" in text or "open tube in text" in text:
            open_youtube()

        elif "open telegram" in text or "open telegram app" in text:
            open_telegram()

        elif "open instagram" in text or "open insta" in text:
            open_insta()

        elif "open chrome" in text or "open google" in text:
            open_chrome()

        elif "open whatsapp" in text or "open what'sapp" in text or "open whats app" in text or "open what's app" in text:
            open_whatsapp()

        elif "open google classroom" in text:
            webbrowser.open("https://classroom.google.com/u/0/")

        elif "open chat GPT" in text or "open chatgpt" in text or "open chat gpt" in text or "open chat gpt" in text:
            open_chat_GPT()

        elif "open google classroom" in text:
            webbrowser.open("https://classroom.google.com/u/0/")

        elif "close" in text or "close this" in text or "close tab" in text:
            speak("closing the current display screen")
            gui.hotkey('alt', 'f4')

        elif text in qa_dict:
            ans = qa_dict[text]
            speak_thread = threading.Thread(target=speak, args=(ans,))
            speak_thread.start()
            speak_thread.join()

        elif "shutdown" in text or "shut down" in text:
            gui.hotkey('win', 'd')
            time.sleep(1)
            gui.hotkey('alt', 'f4')
            time.sleep(1)
            gui.press('enter')

        elif "good morning" in text or "good evening" in text or "good night" in text:
            wish()

        elif "minimise" in text or "minimise the window" in text:
            gui.hotkey('win', 'd')

        elif "play music" in text or "play music on youtube" in text:
            speak("Sir, which song do you want to play?")
            song_name = listen().lower()
            play_music_on_youtube(song_name)
        
        elif "show me the youtube chanel progress" in text or "show me the youtube progress" in text:
            speak("sure sir, which chanel do you want to check?")
            text = listen().lower()
            if "nethyfun" in text:
                NetHyFun_Count()
            elif "night conspiracy" in text:
                Night_Conspiracy_Count()
            elif "nethytoons" in text or "nethy toons" in text or "net hy toons" in text or "net high tunes" in text:
                NetHyToons_Count()
            elif "royal free music" in text or "royal free music ncs" in text or "royal free music ncs" in text:
                Royal_Free_Music_NCS_Count()
                continue
        elif text.startswith(("samy","sami","say me")):
            text.replace("samy","")
            text.replace("sami","")
            prompt = text
            response = chat_with_ai(prompt)

            if not response:
                wiki_search(text)  # If OpenAI response is empty, pass to wiki_search
                return

            # Start animation and speaking concurrently
            animate_thread = threading.Thread(target=print_animated_message, args=(response,))
            speak_thread = threading.Thread(target=speak, args=(response,))

            animate_thread.start()
            speak_thread.start()

            animate_thread.join()
            speak_thread.join()

            # Assuming 'search_text' is defined somewhere
            qa_dict[text] = response  # Store in qa_dict
            save_qa_data(qa_file_path, qa_dict)  # Save updated qa_dict

if __name__ == '__main__':
    main()
