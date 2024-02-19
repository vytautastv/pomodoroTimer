import time
import sys
import os

def pomodoro_timer(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        sys.stdout.write('\r' + timer + ' [' + '#' * (seconds // 60) + ' ' * (minutes - seconds // 60) + ']')
        sys.stdout.flush()
        time.sleep(1)
        seconds -= 1
    print('\nTime is up!')
    # Play a sound when time is up (adjust the path according to your sound file)
    os.system("afplay /System/Library/Sounds/Ping.aiff")

if __name__ == "__main__":
    print("Welcome to the Pomodoro Timer!")
    while True:
        try:
            minutes = int(input("Enter the duration of the Pomodoro session (in minutes): "))
            break
        except ValueError:
            print("Please enter a valid integer.")
            
    pomodoro_timer(minutes)
