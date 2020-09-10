# Import Suitable Library
import string
import random
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image


# Declare CONSTANT VARIABLE
LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation   

# ================================== Function Block ======================================

def password_generator_bychoice(choice_list, length=8):
    '''
    User can choose password character combination which could either be digits, letters, 
    punctuation or combibation of either of them.

    :returns list <class 'list'> of boolean. Defaults to [True, True, True] for invalid choice
        0th list item represents NUMBERS
        1st list item represents LETTERS
        2nd list item represents PUNCTUATION
    '''
    string_constant  = ""
    string_constant += NUMBERS if choice_list[0] else ''
    string_constant += LETTERS if choice_list[1] else ''
    string_constant += PUNCTUATION if choice_list[2] else ''


    # convert string_constant from string to list and shuffle
    string_constant = list(string_constant)
    random.shuffle(string_constant)
    
    try:
        # generate random password and convert to string
        random_password = random.choices(string_constant, k=length)
        random_password = ''.join(random_password)
    except:
        random_password = "Select Checkbox"
        
    return random_password


def press():
    '''
        Function that will be used when Generate button is clicked
    '''

    # Collect all Var from CheckBox into a List 
    choice_list = [bool(_number.get()), bool(_letter.get()), bool(_punctuation.get()) ]

    # when length is '', length for password generator will be default   
    if entry.get() == '':
        label['text'] = password_generator_bychoice(choice_list)

    # Entry Input is Digit
    elif entry.get().isdigit():
        # Get Entry Value
        length = int(entry.get())

        # Set Label Text to password generator return
        label['text'] = password_generator_bychoice(choice_list, length)
    
    # Entry Input is not Digit
    else:
        messagebox.showinfo("Warning", "Length in Numbers Only")
    
    
def checkbutton(app, text, var):
    c = Checkbutton(app, text= text, variable= var)
    return c
    
def imageopen(path, size = (30,30)):
    img = Image.open(path)
    img.thumbnail(size, Image.ANTIALIAS)
    return img

# ======================================== END ======================================

# ============================= Adding Window Components  ===========================

app = Tk()
app.title("Password Generator")
app.iconbitmap("password.ico")

_number = IntVar()
_letter = IntVar()
_punctuation = IntVar()

# ======================================== END ======================================

# ==================================== Main Design ==================================

label = Label(app, text = "Max Length")
label.grid(column = 1)

entry = Entry(app , font=("Calibri",20),justify="right")
entry.grid(row = 1, columnspan = 3, ipadx=5, ipady = 5)
    
cb_letter = checkbutton(app, "Number", _number)
cb_letter.grid(row = 2, column = 0)

cb_string = checkbutton(app, "Letter", _letter)
cb_string.grid(row = 2, column = 1)

cb_punctuation = checkbutton(app, "Punctuation", _punctuation)
cb_punctuation.grid(row = 2, column = 2)

button = Button(app, text = "Generate", command = lambda : press())
button.grid(row = 3, column = 1)

label = Label(app, text = "Hasil", font = 20)
label.grid(row = 4, column = 1)

copy_logo = ImageTk.PhotoImage(imageopen("copy.png"))
button = Button(app, image = copy_logo, command = lambda : copyToClipBoard())
button.grid(row = 4, column = 2)

app.mainloop()
# ======================================== END ======================================
