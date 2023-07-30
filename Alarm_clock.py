import tkinter as tk
from tkinter import messagebox
from pydub import AudioSegment
from pydub.playback import play
import datetime
import time


def set_alarm():
    hour = int(hour_entry.get())
    minute = int(minute_entry.get())
    now = datetime.datetime.now()
    alarm_time = datetime.datetime(now.year, now.month, now.day, hour, minute, 0)

    if now > alarm_time:
        alarm_time += datetime.timedelta(days=1)  # If the alarm time has passed, set it for the next day

    time_diff = alarm_time - now
    total_seconds = time_diff.total_seconds()

    if total_seconds > 0:
        time.sleep(total_seconds)
        messagebox.showinfo("Alarm", "Wake up!")
        sound = AudioSegment.from_file("/Users/athul/Downloads/Alarm.mp3")  # Replace "alarm_sound.mp3" with the path to your sound file
        play(sound)
    else:
        messagebox.showinfo("Alarm", "Invalid time!")


# Create the main window
root = tk.Tk()
root.title("Alarm Clock")

# Create labels and entry fields for hour and minute inputs
hour_label = tk.Label(root, text="Hour:")
hour_label.pack()

hour_entry = tk.Entry(root)
hour_entry.pack()

minute_label = tk.Label(root, text="Minute:")
minute_label.pack()

minute_entry = tk.Entry(root)
minute_entry.pack()

# Create a button to set the alarm
set_alarm_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_alarm_button.pack()

# Run the main loop
root.mainloop()
