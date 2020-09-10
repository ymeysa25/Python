from tkinter import *
import datetime


class CountDown(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.second_left = 0
        self._timer_on = False
        self.create_widgets()
        self.show_widgets()
    
    def show_widgets(self):
        self.label.grid( row = 0)
        self.entry.grid( row = 1)
        self.start.grid( row = 2)
            
    def create_widgets(self):
        
        self.label = Label(self, text = "0:00:00" , font = ("Calibry", 90))
        self.entry = Entry(self, justify = "center")
        
        self.start = Button(self, text = "Start", command = self.start_button)
    
    def countdown(self):
        self.label['text'] = self.convert_seconds_left_to_time()
        
        if self.second_left:
            self.second_left -= 1
            self._timer_on = self.after(1000, self.countdown)
        else:
            self._timer_on = False
            
    def start_button(self):
        self.second_left = int(self.entry.get())
        self.stop_timer()
        self.countdown()
    
    def stop_timer(self):
        if self._timer_on:
            self.after_cancel(self._timer_on)
            self._timer_on = False
    
    def convert_seconds_left_to_time(self):
        return datetime.timedelta(seconds = self.second_left)


if __name__ == '__main__':
    root = Tk()
    root.title("Countdown")
    root.resizable(False, False)
    countdown = CountDown(root)
    countdown.grid()
    root.mainloop()