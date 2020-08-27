# =================================  Importing Suitable Libraries =========================================================
from tkinter import *
from tkinter import messagebox
import random as r
import tkinter.font as font

# ================================================ End  ===================================================================

# ================================== Declaring CONSTANT VARIABLE  =========================================================

# CONTANT VAR
APP_NAME = "Tic Tac Toe"
HEIGHT = 2
WIDTH = 5
colour={'O':"deep sky blue",'X':"lawn green"}
appFont = ('arial',30,'bold')

#DYNAMIC VAR
turn = r.choice(['O','X'])
count = 0

# ===================================== End  ===============================================================

#=================================== function code starts here =============================================

"""
    function for game's rule
"""
def check():
    # Horizontal Check

    # across the top
    if button7['text'] == button8['text'] == button9['text'] == turn: 
        messagebox.showinfo("Congrats!!","'"+turn+"' has won")
        reset()

    # across the middle
    elif button4['text'] == button5['text'] == button6['text'] == turn:
        messagebox.showinfo("Congrats!!","'"+turn+"' has won")
        reset()

    # across the bottom
    elif button1['text'] == button2['text'] == button3['text'] == turn:
        messagebox.showinfo("Congrats!!","'"+turn+"' has won")
        reset()

    # Vertical Check

    # down the left side
    elif button1['text'] == button4['text'] == button7['text'] == turn:
        messagebox.showinfo("Congrats!!","'"+turn+"' has won")
        reset()
    
    # down the middle
    elif button2['text'] == button5['text'] == button8['text'] == turn:
        messagebox.showinfo("Congrats!!","'"+turn+"' has won")
        reset()
    
    # down the right side
    elif button3['text'] == button6['text'] == button9['text'] == turn:
        messagebox.showinfo("Congrats!!","'"+turn+"' has won")
        reset()
    
    # diagonal
    elif button3['text'] == button5['text'] == button7['text'] == turn:
        messagebox.showinfo("Congrats!!","'"+turn+"' has won")
        reset()
    
    # diagonal
    elif button1['text'] == button5['text'] == button9['text'] == turn:
        messagebox.showinfo("Congrats!!","'"+turn+"' has won")
        reset()
    
    # Max turn
    elif count >=9:
        messagebox.showinfo("Tied!!","The match ended in a draw")
        reset()
 
"""
    Function to reset when game is already finished
"""
def reset():
    global turn, count
    button1.config(text=" ", state=NORMAL)
    button2.config(text=" ", state=NORMAL)
    button3.config(text=" ", state=NORMAL)
    button4.config(text=" ", state=NORMAL)
    button5.config(text=" ", state=NORMAL)
    button6.config(text=" ", state=NORMAL)
    button7.config(text=" ", state=NORMAL)
    button8.config(text=" ", state=NORMAL)
    button9.config(text=" ", state=NORMAL)

    turn = r.choice(['O','X'])
    count = 0

"""
    Function that run whenever button is clicked
"""
def click(btn):
    global turn, count
    btn.config(text=turn, state=DISABLED, disabledforeground = colour[turn])
    check()
    turn = "O" if turn == "X" else "X"
    count += 1

"""
    Function to design button widget
"""
def button(frame):
    b = Button(app,text = " ", height = HEIGHT, width = WIDTH , command = lambda :click(b), font = appFont,  bg = 'white')
    return b    

# ===================================== End  ===============================================================

if __name__ == "__main__": 

    # ======================= Adding Window Components  ===========================
    app = Tk()
    app.title(APP_NAME)
    app.iconbitmap("tic-tac-toe.ico")
    app.geometry("390x381")
    app.maxsize(390,381)
    app.minsize(390,381)

    # ================================== End =======================================

    # =========================== Main Design App  =================================
    # I used Grid Manager to manage All Tkinter Widget
    button7 = button(app)
    button7.grid(row = 0, column = 0)

    button8 = button(app)
    button8.grid(row = 0, column = 1)

    button9 = button(app)
    button9.grid(row = 0, column = 2)

    button4 = button(app)
    button4.grid(row = 1, column = 0)

    button5 = button(app)
    button5.grid(row = 1, column = 1)

    button6 = button(app)
    button6.grid(row = 1, column = 2)

    button1 = button(app)
    button1.grid(row = 2, column = 0)

    button2 = button(app)
    button2.grid(row = 2, column = 1)

    button3 = button(app)
    button3.grid(row = 2, column = 2)

    
    #load the window 
    app.mainloop()

    # ================================== End =======================================

