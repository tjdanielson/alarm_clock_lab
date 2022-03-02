from AlarmClock import AlarmClock

alarm_clock_one = AlarmClock()

#print original current clock's time to the terminal
print(alarm_clock_one.current_time)

#change the time
alarm_clock_one.set_time()

#toggle alarm clock's on/off switch (and print new on/off status to terminal)
alarm_clock_one.toggle_alarm()

#set the alarm time
alarm_clock_one.set_alarm()