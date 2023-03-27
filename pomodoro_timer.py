import tkinter as tk
import time
import sys 

# Platform-specific sound settings
if sys.platform.startswith('darwin'):
    sound_file = '/System/Library/Sounds/Glass.aiff'  # Mac sound file
else:
    sound_file = 'SystemExclamation'  # Windows sound alias

# Pomodoro timer settings
work_time = 25 * 60  # 25 minutes of work
break_time = 5 * 60  # 5 minutes of break
cycles = 4  # default number of cycles

# GUI creation
root = tk.Tk()
root.title("Pomodoro Timer")
root.geometry("400x400")

# Label to display remaining time
time_label = tk.Label(root, text="", font=("Helvetica", 48))
time_label.pack(pady=50)

# Button to start the timer
def start_timer():
    num_cycles = cycle_var.get()  # get the number of cycles from the radio button
    for i in range(num_cycles):
        time_label.config(text="Work")
        countdown(work_time)
        play_sound(sound_file)  # play a sound when work is done
        time_label.config(text="Break")
        countdown(break_time)
        play_sound(sound_file)  # play a sound when break is done
    time_label.config(text="Pomodoro complete!")

# Function to countdown the timer
def countdown(t):
    while t:
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs)
        time_label.config(text=timer)
        root.update()
        time.sleep(1)
        t -= 1


# Function to play a sound
def play_sound(sound):
    if sys.platform.startswith('darwin'):
        import subprocess
        subprocess.Popen(['afplay', sound])  # play sound on Mac 
    else:
        import winsound
        winsound.PlaySound(sound, winsound.SND_ALIAS)  # play sound on Windows

# Radio buttons to select number of cycles
cycle_var = tk.IntVar()
cycle_var.set(cycles)
cycle_frame = tk.Frame(root)
cycle_frame.pack()
cycle_label = tk.Label(cycle_frame, text="Number of cycles:")
cycle_label.pack(side=tk.LEFT, padx=10)
one_cycle = tk.Radiobutton(cycle_frame, text="1", variable=cycle_var, value=1)
one_cycle.pack(side=tk.LEFT)
two_cycles = tk.Radiobutton(cycle_frame, text="2", variable=cycle_var, value=2)
two_cycles.pack(side=tk.LEFT)
four_cycles = tk.Radiobutton(cycle_frame, text="4", variable=cycle_var, value=4)
four_cycles.pack(side=tk.LEFT)
six_cycles = tk.Radiobutton(cycle_frame, text="6", variable=cycle_var, value=6)
six_cycles.pack(side=tk.LEFT)
eight_cycles = tk.Radiobutton(cycle_frame, text="8", variable=cycle_var, value=8)
eight_cycles.pack(side=tk.LEFT)
ten_cycles = tk.Radiobutton(cycle_frame, text="10", variable=cycle_var, value=10)
ten_cycles.pack(side=tk.LEFT)

# Button to start the timer
start_button = tk.Button(root, text="Start", font=("Helvetica", 24), command=start_timer)
start_button.pack(pady=30)

# Run the app
root.mainloop()