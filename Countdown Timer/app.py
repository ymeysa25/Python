from tkinter import *
import datetime


from PIL import ImageTk
from PIL import Image

_timer_on = False

second_left = 0

bg = 'black'


def imageopen(path, size = (30,30)):
    img = Image.open(path)
    img.thumbnail(size, Image.ANTIALIAS)
    return img

def start_button():
    global second_left
    
    second_left = int(entry.get())
    stop_timer()
    countdown()

def stop_timer():
    global _timer_on
    if _timer_on:
        app.after_cancel(_timer_on)
        _timer_on = False
        
def countdown():
    global _timer_on, second_left
#     _timer_on = True
    label['text'] = convert_seconds_left_to_time(second_left)
    
    if second_left:
        second_left -= 1
        _timer_on = app.after(1000, countdown)
    else:
        _timer_on = False
            
def breakline(row):
    Label(app, text = '\n' , bg = bg).grid(row = row)
    
        
def convert_seconds_left_to_time(second):
    return datetime.timedelta(seconds = second)

    
app = Tk()
app.title("Countdown Timer")
app.config(bg = bg) 

intVar = IntVar()
label = Label(app, text = "0:00:00", bg = bg, fg = 'white', font = ("Calibry", 90))
label.grid(row = 0)

entry = Entry(app, justify = "center", bg = 'white', fg = 'black')
entry.grid(row = 1)

breakline(2)
play_logo = ImageTk.PhotoImage(imageopen("play.png"))
button = Button(app, text = "start", command = start_button, bg = bg, image = play_logo)
button.grid(row = 3)
breakline(4)

app.mainloop()