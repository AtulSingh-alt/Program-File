# Create a countdown timer
import time

def countdown(sec):
    while sec:
        mins,secs = divmod(sec,60)
        time_format = "{:02d}:{:02d}".format(mins,secs)
        print(time_format)
        time.sleep(1)
        sec = sec-1
    print("Stop")

countdown(10)
