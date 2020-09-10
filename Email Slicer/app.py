from tkinter import *
from tkinter import messagebox

app = Tk()
app.title("Email Slicer")
app.geometry("300x110")

def press():
    text = entry.get()
    result = email_slicer(text)
    if result[2]:
        user_label['text'] = "Name : " + result[0]
        domain_label['text'] = "Domain : " + result[1]
    else:
        user_label['text'] = result[0]
        domain_label['text'] = result[1]
        
    
def email_slicer(text):
    try:
        return text[:text.index("@")], text[text.index("@") + 1:], True
    except:
        return "Sorry","Please input in email format", False
    
label = Label(app, text = "Find username and domain")
label.pack()

entry = Entry(app)
entry.pack()

btn = Button(app, text = "start", command = press)
btn.pack()

user_label = Label(app)
user_label.pack()

domain_label = Label(app)
domain_label.pack()

app.mainloop()
