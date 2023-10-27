import os
import json
import requests
from apscheduler.schedulers.background import BackgroundScheduler
import tkinter as tk

def NetHyFun_Count():
    # Replace with your own YouTube Data API key
    API_KEY = 'AIzaSyCmvzhf8sQydT_o1SIp0inVqPRK0zEF36w'

    # Replace with the channel ID you want to track
    CHANNEL_ID = 'UC27FbPjZWNRNdfJ-TZmOCaQ'

    Chanel_Name = "NetHyFun"

    # Function to get the subscriber count for a specific channel
    def get_subscriber_count():
        url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={CHANNEL_ID}&key={API_KEY}'
        response = requests.get(url)
        data = json.loads(response.text)
    
        if 'items' in data:
            subscriber_count = int(data['items'][0]['statistics']['subscriberCount'])
            subscriber_label.config(text=f'{Chanel_Name}, Subscribers: {subscriber_count}')

    # Create a scheduler to run the function every 30 seconds
    scheduler = BackgroundScheduler()
    scheduler.add_job(get_subscriber_count, 'interval', seconds=0)

    # Start the scheduler
    scheduler.start()

    # Create a simple GUI
    root = tk.Tk()
    root.title("NetHyFun Subscriber Count")

    subscriber_label = tk.Label(root, text="", font=("Arial", 14))
    subscriber_label.pack(pady=20)

    root.mainloop()



def Night_Conspiracy_Count():
    # Replace with your own YouTube Data API key
    API_KEY = 'AIzaSyCmvzhf8sQydT_o1SIp0inVqPRK0zEF36w'

    # Replace with the channel ID you want to track
    CHANNEL_ID = 'UC7YDMgu0dMRZotLMuB3oEcQ'

    Chanel_Name = "Night_Conspiracy"

    # Function to get the subscriber count for a specific channel
    def get_subscriber_count():
        url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={CHANNEL_ID}&key={API_KEY}'
        response = requests.get(url)
        data = json.loads(response.text)
    
        if 'items' in data:
            subscriber_count = int(data['items'][0]['statistics']['subscriberCount'])
            subscriber_label.config(text=f'{Chanel_Name}, Subscribers: {subscriber_count}')

    # Create a scheduler to run the function every 30 seconds
    scheduler = BackgroundScheduler()
    scheduler.add_job(get_subscriber_count, 'interval', seconds=0)

    # Start the scheduler
    scheduler.start()

    # Create a simple GUI
    root = tk.Tk()
    root.title("Night_Conspiracy Subscriber Count")

    subscriber_label = tk.Label(root, text="", font=("Arial", 14))
    subscriber_label.pack(pady=20)

    root.mainloop()

def NetHyToons_Count():
    # Replace with your own YouTube Data API key
    API_KEY = 'AIzaSyCmvzhf8sQydT_o1SIp0inVqPRK0zEF36w'

    # Replace with the channel ID you want to track
    CHANNEL_ID = 'UCMojX78Utgt6pxScBSH6mjg'

    Chanel_Name = "NetHyToons"

    # Function to get the subscriber count for a specific channel
    def get_subscriber_count():
        url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={CHANNEL_ID}&key={API_KEY}'
        response = requests.get(url)
        data = json.loads(response.text)
    
        if 'items' in data:
            subscriber_count = int(data['items'][0]['statistics']['subscriberCount'])
            subscriber_label.config(text=f'{Chanel_Name}, Subscribers: {subscriber_count}')

    # Create a scheduler to run the function every 30 seconds
    scheduler = BackgroundScheduler()
    scheduler.add_job(get_subscriber_count, 'interval', seconds=0)

    # Start the scheduler
    scheduler.start()

    # Create a simple GUI
    root = tk.Tk()
    root.title("NetHyToons Subscriber Count")

    subscriber_label = tk.Label(root, text="", font=("Arial", 14))
    subscriber_label.pack(pady=20)

    root.mainloop()    


def Royal_Free_Music_NCS_Count():
    # Replace with your own YouTube Data API key
    API_KEY = 'AIzaSyCmvzhf8sQydT_o1SIp0inVqPRK0zEF36w'

    # Replace with the channel ID you want to track
    CHANNEL_ID = 'UCuOwdl-LCDAu3RcHmYtUx9w'

    Chanel_Name = "Royal Free Music - NCS"

    # Function to get the subscriber count for a specific channel
    def get_subscriber_count():
        url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={CHANNEL_ID}&key={API_KEY}'
        response = requests.get(url)
        data = json.loads(response.text)
    
        if 'items' in data:
            subscriber_count = int(data['items'][0]['statistics']['subscriberCount'])
            subscriber_label.config(text=f'{Chanel_Name}, Subscribers: {subscriber_count}')

    # Create a scheduler to run the function every 30 seconds
    scheduler = BackgroundScheduler()
    scheduler.add_job(get_subscriber_count, 'interval', seconds=0)

    # Start the scheduler
    scheduler.start()

    # Create a simple GUI
    root = tk.Tk()
    root.title("Royal Free Music - NCS Subscriber Count")

    subscriber_label = tk.Label(root, text="", font=("Arial", 14))
    subscriber_label.pack(pady=20)

    root.mainloop()    

