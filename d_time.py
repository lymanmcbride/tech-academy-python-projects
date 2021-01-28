import datetime
import pytz

portland = pytz.timezone('US/Pacific')
nyc = pytz.timezone('US/Eastern')
london = pytz.timezone('Europe/London')

def get_times(portland, nyc, london):
    current_time = datetime.datetime.now()
    portland_time = current_time.astimezone(portland)
    nyc_time = current_time.astimezone(nyc)
    london_time = current_time.astimezone(london)
    return portland_time, nyc_time, london_time

def compare(portland, nyc, london):
    portland_time, nyc_time, london_time = get_times(portland, nyc, london)
    branches = {"Portland": portland_time, "New York": nyc_time, "London": london_time}
    for branch in branches.keys():
        o = True
        current_hour = int(branches[branch].time().strftime('%H'))
        current_time = branches[branch].time().strftime('%H:%M')
        if current_hour < 9 or current_hour > 17:
            o = False
        if o:
            print("The {} branch is open! The time there is {}".format(branch, current_time))
        else:
            print("The {} branch is closed! The time there is {}".format(branch, current_time))
            


compare(portland, nyc, london)