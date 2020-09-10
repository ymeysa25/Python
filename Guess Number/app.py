from tkinter import *
from tkinter import messagebox
import random as rn



constrain = "=================================="
columnspan = 5
guess_count = 0
max_guess = 3
guess_status = lambda x,y : f"Number of Guesses : {x}          Max of Guess : {y}"
bg = 'white'
guess_number = rn.randint(0,10)

app = Tk()
app.title("GUESS NUMBER")
app.config(bg= bg)

def game(number): 
    global guess_number, guess_count
    result = ''
    color = ''
    won = False
    
    if number == guess_number:
        result = "Your Guess is Right, You Won!!"
        color = 'green'
        won = True
    elif number < guess_number:
        result = "Secret number is more than your current guess!!"
        color = 'red'
    elif number > guess_number:
        result = "Secret number is less than your current guess!!"
        color = 'red'
    else:
        result = "WRONG INPUT"
    
    return result, color, won

def MyLabel(app, text, fg = 'black'):
    l = Label(app, text = text, bg = bg, fg = fg)
    return l

def button(frame, text):          #Function to define a button
    b=Button(frame, padx=1,width=3,text= text,bd=2 , bg = bg)
    return b

def reset():
    global guess_count, guess_number
    for i in range(3):
        hint[i]['text'] = ''
        
    for i in range(2):
        for j in range(5):
            b[i][j].config(state = NORMAL)
    
    guess_count = 0
    guess_number = rn.randint(0,10)
    lb_number_guess['text'] = guess_status(guess_count, max_guess)
    
def disablebutton():
    for i in range(2):
        for j in range(5):
            b[i][j].config(state = DISABLED)
    
def press(row, column):
    global guess_count
    text = b[row][column]['text']
    result = game(int(text))

        
    hint[guess_count].config(text = result[0], fg = result[1])
    guess_count +=1
    lb_number_guess['text'] = guess_status(guess_count, max_guess)
    
        
    if guess_count == 3:
        disablebutton()
        if result[2] is False:
            messagebox.showinfo("Game", "You Lose")
    if result[2]:
        disablebutton()
        
    

    
label = MyLabel(app, text = "Guess Number between 1 and 10")
label.grid(row = 0, column = 0, columnspan = columnspan)

lb_constrain = MyLabel(app, text = constrain)
lb_constrain.grid(row = 1, column = 0, columnspan = columnspan)

lb_number_guess = MyLabel(app, text = guess_status(guess_count, max_guess))
lb_number_guess.grid(row = 2, columnspan = columnspan)

lb_constrain = MyLabel(app, text = constrain)
lb_constrain.grid(row = 3, column = 0, columnspan = columnspan)



# ================================ HINT LABEL ====================
label = MyLabel(app, text = "HINT")
label.grid(row = 4, column = 0, columnspan = columnspan)

hint = []

for i in range(3):
    hint.append(MyLabel(app, ""))
    hint[i].grid(row = i + 5, column = 0, columnspan = columnspan)
    
lb_constrain = MyLabel(app, text = constrain)
lb_constrain.grid(row = 8, column = 0, columnspan = columnspan)
# ================================ END =======================


# ================================ Number =======================

b=[[],[],[], [], []]
count = 1
for i in range(2):
        for j in range(5):
            b[i].append(button(app, count))
            b[i][j].config(command= lambda row=i,col=j:press(row,col))
            b[i][j].grid(row=i + 9,column=j)
            count +=1

# ================================ END =======================

            
lb_constrain = MyLabel(app, text = constrain)
lb_constrain.grid(row = 11, columnspan = columnspan)

btn_restart = Button(app, text = "Restart Game", bg = bg, command = lambda : reset())
btn_restart.grid(row = 12, columnspan = columnspan  )
app.mainloop()