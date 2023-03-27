# Pomodoro Timer
This is a simple Pomodoro Timer app that allows you to select the number of cycles you want to complete (up to 10) and plays a sound when each cycle is finished. It uses a graphical user interface (GUI) created with the Python tkinter module.

## Getting Started
### Prerequisites
To run this program, you need to have Python 3 installed on your computer.

### Running the Program
1. Download or clone this repository to your computer.

2. Open a terminal or command prompt window and navigate to the directory where you saved the repository.

3. Run the following command to start the program:
> python pomodoro_timer.py

4. The GUI should appear, and you can select the number of cycles you want to complete and click the "Start" button to begin the timer.

## Customization
You can customize the following settings in the pomodoro_timer.py file:

work_time: The length of each work period (in seconds).
break_time: The length of each break period (in seconds).
cycles: The default number of cycles to complete if the user doesn't select a different value.
You can also customize the sound file that plays when each cycle is finished by changing the sound_file variable in the play_sound() function.
