#!/usr/bin/env python3
import os
import datetime
import time

def duck_alarm():
    print("Quack! Quack! It's time to wake up!")

def main():
    while True:
        current_time = datetime.datetime.now().time()

        # Set your alarm times
        gym_time = datetime.time(5, 0)
        kids_wake_up_time = datetime.time(6, 0)
        leave_for_school_time = datetime.time(7, 0)

        if current_time < gym_time:
            time_until_alarm = (datetime.datetime.combine(datetime.date.today(), gym_time) -
                               datetime.datetime.now()).seconds
            if time_until_alarm <= 300:
                duck_alarm()
                break

        elif current_time < kids_wake_up_time:
            time_until_alarm = (datetime.datetime.combine(datetime.date.today(), kids_wake_up_time) -
                               datetime.datetime.now()).seconds
            if time_until_alarm <= 300:
                duck_alarm()
                break

        elif current_time < leave_for_school_time:
            time_until_alarm = (datetime.datetime.combine(datetime.date.today(), leave_for_school_time) -
                               datetime.datetime.now()).seconds
            if time_until_alarm <= 300:
                duck_alarm()
                break

        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()

