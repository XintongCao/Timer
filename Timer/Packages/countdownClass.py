import time
import datetime
import easygui
class Countdown():
    # input for hours,minutes, and seconds for the timer
    def __init__(self):
        text='Please set a time limit for your Countdown Timer: '
        global title
        title='Window of Countdown Timer'
        #list of multiple inputs
        time_input_list=['Hours: ','Minutes: ','Seconds: ']
        default_list=['eg.,0-9...','eg.,0-99...','eg.,0-999...']
        #create a multiple enter box
        output=easygui.multenterbox(text,title,time_input_list,default_list)

        msg=f'Entered details of the time limit: {str(output[0])} hours {str(output[1])} minutes {str(output[2])} seconds.'
        easygui.msgbox(msg,title)

        self.h=str(output[0])
        self.m=str(output[1])
        self.s=str(output[2])

        self.countdown()
    #create class that acts as a countdown
    def countdown(self):
        #calculate the total numbers of the seconds
        total_seconds=int(self.h)*3600+int(self.m)*60+int(self.s)
        # while loop that checks if the total_seconds reaches zero
        # if not zero, decrement total left time by 1 second
        while total_seconds>0:
            # timer presents the left time on countdown timer
            timer=datetime.timedelta(seconds=total_seconds)
            # print the time left on the timer
            print(timer,end='\r')
            #delays the App by 1-second
            time.sleep(1)
            #reduces total time by 1-second
            total_seconds=total_seconds-1

        easygui.msgbox('Bzzzt!!! The countdown Timer is at ZERO second!!',title)
