import easygui
import sys
from Packages.countdownClass import Countdown
from Packages.stopwatchClass import Stopwatch
class Main():
    
    def __init__(self):

        while True:
            easygui.msgbox('Welcome to Timer!','Loading...')
            # define msg,title,and choices
            msg='Please select the type of the timers: '
            title='Type of Timers'
            choices=['Countdown Timer','Stopwatch(Lap Timer)','Exit']
            #set the button-box
            button=easygui.buttonbox(msg,title,choices)
            #note that we convert the choices to string
            #if the users cancelled the choices, and we got None
            easygui.msgbox(f'You chose the Timer: {str(button)}','Loading...')

            text=f'Want to start the {str(button)} right now?'
            title1='Please Enter Your Option: '
            #show a Cancel\Continue dialog
            if easygui.ccbox(text,title1):
                #user chose Continue
                if str(button)==choices[0]:
                    Countdown()
                elif str(button)==choices[1]:
                    Stopwatch()
                else:
                    easygui.msgbox('Exit Success!','Exiting')
                    sys.exit(0)
            else:
                #user chooses Cancel
                sys.exit(0)


if __name__=='__main__':
    Main()
