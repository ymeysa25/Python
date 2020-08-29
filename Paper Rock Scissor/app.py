from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
import time
from tkinter import messagebox
import random as rn



key = ("Rock", "Paper", "Scissor")
path = [f"Assets/{key[i]}.png" for i in range(3)]
size = 128, 128

player = ''
gameresult = ''
computers = key[rn.randint(0,2)]

def press(row):
    global player
    reset()
    player = key[int(row)]
    btn[key.index(computers)].config(state=DISABLED)
    rule(player, computers)
    label.config(image = '', text = gameresult, font = 5, height = 6)
    
    
#     messagebox.showinfo("Game", text)

def rule(player, computer):
    global computers, gameresult
    if player == computer:
        gameresult = "Tie!"
    elif player == key[0]:
        if computer == key[1]:
            gameresult = "You lose! \n" + computer + " covers " + player
        else:
            gameresult =  "You win! \n" + player +  " smashes " + computer
    elif player == key[1]:
        if computer == key[2]:
            gameresult = "You lose! \n" + computer + " cut " + player
        else:
            gameresult = "You win! \n" + player + " covers " + computer
    elif player == key[2]:
        if computer == key[0]:
            gameresult = "You lose... \n" + computer + " smashes " + player
        else:
            gameresult = "You win! \n" + player + " cut " +  computer
    else:
        print("That's not a valid play. Check your spelling!")
    
    computers = key[rn.randint(0,2)]

def imageopen(path):
    img = Image.open(path)
    img.thumbnail(size, Image.ANTIALIAS)
    return img
    
def reset():
    for i in range(3):
        btn[i].config(state = NORMAL)
btn =[]
img = []

app = Tk()
app.title("Rock Paper Scissor")
app.config(bg = 'white')


title = Label(app, text = "Paper Rock Scissor Game" ,bg = 'white')
title.grid(row = 0, column= 1)

for i in range(3):
    img.append(ImageTk.PhotoImage(imageopen(path[i])))
    btn.append(Label(app, bg = 'white', text = key[i]))
    btn[i].config(image = img[i])
    btn[i].grid(row = 1, column = i)
    
labelimg = ImageTk.PhotoImage(imageopen("Assets/vs.png"))
label = Label(app, image = labelimg, bg = 'white')
label.grid(row = 2, column= 0, columnspan = 3)

btn2 = []
for i in range(3):
    btn2.append(Button(app, bg = 'white', text = key[i], command = lambda row = i: press(row)))
    btn2[i].config(image = img[i])
    btn2[i].grid(row = 3, column = i)
app.mainloop()
