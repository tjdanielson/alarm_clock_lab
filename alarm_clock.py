
class AlarmClock:

    def __init__(self):
        self.current_time = '12:00 AM'
        self.alarm_on = False
        self.alarm_time = ''

    def set_time(self):
        self.current_time = input('What time is it? ')
        print('The current time is: ' + self.current_time)

    def toggle_alarm(self):
        if self.alarm_on == False:
            self.alarm_on = True
            print('Your alarm is now ON')
        else:
            self.alarm_on = False
            print('Your alarm is now OFF')
    
    def set_alarm(self):
        self.alarm_time = input('What time do you want your alarm to ring? ')
        print('Your alarm is set for: ' + self.alarm_time)