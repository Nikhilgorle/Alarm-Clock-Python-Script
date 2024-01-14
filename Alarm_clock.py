from datetime import datetime
from playsound import playsound

alarm_time=input("enete the time of alarm in 12 hour format with specifying AM or PM:HH:MM:SS\n")
alarm_hour=alarm_time[:2]
alarm_minute=alarm_time[3:5]
alarm_second=alarm_time[6:8]
alarm_peroid=alarm_time[9:11].upper()

audio_file_path = r'd:\_6th\projects\Alarm-Clock-Python-Script\audio.wav'

while True:
    now=datetime.now()
    current_hour=now.strftime("%I")
    current_min=now.strftime("%M")
    current_sec=now.strftime("%S")
    current_period=now.strftime("%p")
    if current_period==alarm_peroid:
        if current_hour==alarm_hour:
            if current_min==alarm_minute:
                if current_sec==alarm_second:
                    print("wake up")
                    playsound(audio_file_path)
                    break