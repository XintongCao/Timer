import time
import easygui
import sys

class Stopwatch():
    def __init__(self):
        # time starts
        start_time=time.time()
        self.start_time=start_time
        last_time=start_time
        self.last_time=last_time
        lapnum=1
        self.lapnum=lapnum
        value=''
        self.value=value

        # define title, msg and button for the button box
        global title
        title='Windown of Stopwatch (Lap Timer)'
        msg='Press ENTER to start a lap!'
        choices=['ENTER']
        easygui.buttonbox(msg,title,choices)

        self.stopwatch()
    # 显示欢迎界面
    def stopwatch(self):
        while self.value!='Q':
            #input for the ENTER key press:
            text='Type any keys and press OK to pause. \nType Q and press OK to stop: '
            d_text='Enter here...'
            self.value=easygui.enterbox(text,title,d_text)

            #user chose to pause the timer and check the time
            msg=f'You entered {str(self.value)} and chose to check the stopwatch results now? '
            easygui.msgbox(msg,title)

            # the current lap-time
            laptime=round(time.time()-self.last_time,2)
            #total time elapsed since the timer started
            totaltime=round(time.time()-self.start_time,2)
            
            #show the results of lapnum,laptime,and totaltime
            title_output='Below shows the results of this lap: '
            msg_output=f'Lap NO. {self.lapnum}. \nLap Time: {laptime}. \nTotal Time: {totaltime}.'
            easygui.msgbox(msg_output,title_output)

            #update the previous lapnum and totaltime
            self.last_time=time.time()
            self.lapnum=self.lapnum+1

        easygui.msgbox('Timing Complete!!',title)
