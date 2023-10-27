import psutil
import time
from playsound import playsound
from speak import speak

def battery_alert():
    while True:
     battery = psutil.sensors_battery()
     percent = int(battery.percent)

     if percent < 30 :
        speak("sir, your Samy is running very low battery. please charge it")

     elif percent < 10:
        speak("sir,this is last chance. your battery is very low")
        playsound("C:\\Users\\Anubhav\\OneDrive\\Desktop\\Samy_3.0\\mp3\\discharged-battery-151926.mp3")   

     elif percent == 100:
        speak("sir, your battery is full")  

     else:
        pass

     time.sleep(60)  


def battey_persentage():
   battery = psutil.sensors_battery()
   percent = int(battery.percent)

   speak(f"the device is running on {percent}% battery power")
