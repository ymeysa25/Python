from tkinter import *
import tkinter.font as font

# CONSTANT VALUE
# WIDGET SIZE
BTN_HEIGHT = 1
BTN_WEIGHT = 6
FONT_SIZE = 21

#WIDGET COLOUR
BTN_BG = 'white'
BTN_FG = 'black'
BTN_KEY_BG = "#a6a6a6"

key = ["+", "-", "/","*"]

expression = "" 

def press(num): 
    # point out the global expression variable 
    global expression 
    
    # To make sure, there ir no duplicate key     
    if num in key and expression[-1] in key:
        expression = expression       
    else:
        # concatenation of string 
        expression = expression + str(num) 
    
    # update the expression by using set method 
    equation.set(expression) 

# Function to clear content
def clear():  
    global expression 
    expression = "" 
    equation.set("0") 
    
def equalpress(): 
    try: 
        global expression 
        if expression[-1] in key:
            expression = expression.replace(expression[-1], " ")
        if expression[0] in key:
            expression = expression.replace(expression[0], " ")
        total = str(eval(expression)) 
        equation.set(total) 
        expression = "" 
    except ZeroDivisionError:
        equation.set(" Can't divide by Zero ") 
        expression = "" 
    except: 
        equation.set(" error ") 
        expression = "" 
    
if __name__ == "__main__": 
    gui = Tk()
    gui.title("Calculator")    
    myFont = font.Font(size=FONT_SIZE)
    equation = StringVar()
    
    expression_field = Entry(gui, textvariable=equation , font=("Calibri",20),justify="right", bg="black",fg="white")
    expression_field.grid(columnspan=4, ipadx=70, ipady = 30) 
    equation.set('0') 
    
    button_plus = Button(gui, text=' + ', fg=BTN_FG, bg=BTN_KEY_BG, 
                     command=lambda: press("+"), height=BTN_HEIGHT, width=BTN_WEIGHT) 
    button_plus['font'] = myFont
    
    button_plus.grid(row=1, column=0) 
    
    button_minus = Button(gui, text=' - ', fg=BTN_FG, bg=BTN_KEY_BG, 
                     command=lambda: press("-"), height=BTN_HEIGHT, width=BTN_WEIGHT) 
    button_minus['font'] = myFont
    
    button_minus.grid(row=1, column=1) 
    
    button_multiply = Button(gui, text=' x ', fg=BTN_FG, bg=BTN_KEY_BG, 
                     command=lambda: press("*"), height=BTN_HEIGHT, width=BTN_WEIGHT) 
    button_multiply['font'] = myFont
    
    button_multiply.grid(row=1, column=2)
    
    button_divide = Button(gui, text=' / ', fg=BTN_FG, bg=BTN_KEY_BG, 
                     command=lambda: press("/"), height=BTN_HEIGHT, width=BTN_WEIGHT) 
    button_divide['font'] = myFont
    
    button_divide.grid(row=1, column=3)
    
    button_equal = Button(gui, text=' = ', fg=BTN_FG, bg="#ff8b3d", 
                     command=equalpress, height= 7, width=BTN_WEIGHT) 
    button_equal['font'] = myFont
    
    button_equal.grid(row=2, column=3, columnspan=2, rowspan=4)
    
    # First Row
    button7 = Button(gui, text=' 7 ', fg=BTN_FG, bg=BTN_BG, 
                     command=lambda: press(7), height=BTN_HEIGHT, width=BTN_WEIGHT) 
    button7['font'] = myFont
    
    button7.grid(row=2, column=0) 
    
    button8 = Button(gui, text=' 8 ', fg=BTN_FG, bg=BTN_BG, 
                     command=lambda: press(8), height=BTN_HEIGHT, width=BTN_WEIGHT) 
    button8['font'] = myFont
    
    button8.grid(row=2, column=1)
    
    button9 = Button(gui, text=' 9 ', fg=BTN_FG, bg=BTN_BG, 
                     command=lambda: press(9), height=BTN_HEIGHT, width=BTN_WEIGHT) 
    button9['font'] = myFont
    
    button9.grid(row=2, column=2)
    
    # Second Row
    button4 = Button(gui, text=' 4 ', fg=BTN_FG, bg=BTN_BG, 
                     command=lambda: press(4), height=BTN_HEIGHT, width=BTN_WEIGHT) 
    button4['font'] = myFont
    
    button4.grid(row=3, column=0) 

    button5 = Button(gui, text=' 5 ', fg=BTN_FG, bg=BTN_BG, 
                     command=lambda: press(5), height=BTN_HEIGHT, width=BTN_WEIGHT) 
    button5['font'] = myFont
    
    button5.grid(row=3, column=1) 
    
    button6 = Button(gui, text=' 6 ', fg=BTN_FG, bg=BTN_BG, 
                     command=lambda: press(6), height=BTN_HEIGHT, width=BTN_WEIGHT) 
    button6['font'] = myFont
    
    button6.grid(row=3, column=2) 
    
    # Third Row
    button1 = Button(gui, text=' 1 ', fg=BTN_FG, bg=BTN_BG, 
                     command=lambda: press(1), height=BTN_HEIGHT, width=BTN_WEIGHT) 
    button1['font'] = myFont
    
    button1.grid(row=4, column=0)
    
    button2 = Button(gui, text=' 2 ', fg=BTN_FG, bg=BTN_BG, 
                     command=lambda: press(2), height=BTN_HEIGHT, width=BTN_WEIGHT) 
    button2['font'] = myFont
    
    button2.grid(row=4, column=1)
    
    button3 = Button(gui, text=' 3 ', fg=BTN_FG, bg=BTN_BG, 
                     command=lambda: press(3), height=BTN_HEIGHT, width=BTN_WEIGHT) 
    button3['font'] = myFont
    
    button3.grid(row=4, column=2)
    
    # Fourth Row
    button0 = Button(gui, text=' 0 ', fg=BTN_FG, bg=BTN_BG, 
                     command=lambda: press(0), height=BTN_HEIGHT, width=BTN_WEIGHT) 
    button0['font'] = myFont
    
    button0.grid(row=5, column=0)
    
    button_dot = Button(gui, text=' . ', fg=BTN_FG, bg=BTN_BG, 
                     command=lambda: press("."), height=BTN_HEIGHT, width=BTN_WEIGHT) 
    button_dot['font'] = myFont
    
    button_dot.grid(row=5, column=1)
    
    button_C = Button(gui, text=' C ', fg=BTN_FG, bg=BTN_BG, 
                     command=lambda: clear(), height=BTN_HEIGHT, width=BTN_WEIGHT) 
    button_C['font'] = myFont
    
    button_C.grid(row=5, column=2)
    

    
    gui.mainloop()