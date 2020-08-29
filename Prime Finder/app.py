from tkinter import *
from tkinter import messagebox
import tkinter.font as font

BTN_WIDTH = 15
BTN_HEIGHT = 2
FONT_SIZE = 20
def primeCheck(num):
    status = False
    if num == 2:
        return True
    
    for i in range(2, num):
        if num % i == 0:
            status = False
            break
        else:
            status = True
    return status

def evenOddCheck(num):
    return True if num % 2 == 0 else False    

def positiveNegativeCheck(num):
    return True if num > 0 else False

def btnClick(btn):
    try:
        num = int(entry.get())
        
        if btn['text'] == "Check Prime":
            prime = primeCheck(num)
            status = " is PRIME Number" if prime else " is NOT prime Number"
            messagebox.showinfo("Prime", str(num) +  status)
            
        elif btn['text'] == "Check Even":
            even = evenOddCheck(num)
            status = " is Even Number" if even else " is Odd Number"
            messagebox.showinfo("Even Odd", str(num) +  status)
            
        elif btn['text'] == "Check Positif":
            positif = positiveNegativeCheck(num)
            status = " is Positif integer" if positif else " is Negatif integer"
            messagebox.showinfo("Positive Negative", str(num) +  status)
            
            
            
    except ValueError:
        pass
#         messagebox.showinfo("Warning!!", "Input number only")
if __name__ == "__main__": 
    app = Tk()
    app.title("Prime Finder")
    app.configure(bg='#192E5B')
    # app.geometry("700x300")
    # 

    entry = Entry(app, textvariable = "Set Number",font=("Calibri",20), justify="right", bg="#1D65A6",fg="white", width = 21)
    entry.grid(row=0, column=0, columnspan=2, ipady = 30) 

    btn = Button(app, text = "Check Prime", bg="#F2A102",fg="black", command = lambda : btnClick(btn), height = (BTN_HEIGHT * 2) + 1, width = BTN_WIDTH)
    btn.grid(row=1, column=1 ,columnspan=2, rowspan=2)
    btn['font'] = FONT_SIZE

    btn1 = Button(app, text = "Check Even" ,bg="#72A2C0",fg="black", command = lambda : btnClick(btn1) , height = BTN_HEIGHT, width = BTN_WIDTH)
    btn1.grid(row=1, column=0) 
    btn1['font'] = FONT_SIZE

    btn2 = Button(app, text = "Check Positif" ,bg="#72A2C0",fg="black", command = lambda : btnClick(btn2), height = BTN_HEIGHT, width = BTN_WIDTH)
    btn2.grid(row=2, column=0) 
    btn2['font'] = FONT_SIZE
    app.mainloop()