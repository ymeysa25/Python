from tkinter import *
from tkinter import messagebox

height = 6
width = 12
choices = ['Hour','Minute','Second']
def press(info, status = "add"):
    global value
    _from = fromvar.get().lower()
    _to = tovar.get().lower()
    if value == '0':
        value = ''
    if status == "add":
        value += str(info)
    else:
        value = str(info)
    label_value['text'] = value
    label_result['text'] = round(timeconverter(eval(value), _from = _from, _to = _to), 3)
    
    
def button(app, index, func):
    b = Button(app,text = index, height = height, width = width, command = lambda : func(index), bg = 'white')
    return b


def ce(*args):
    global value
    value = ''
    label_value['text'] = 0
    label_result['text'] = 0
    
    
def dropDown(*args):
    global value
    press(value, status = "drop")


def del_(*args):
    global value
    value = value[:-1] if value[:-1] != '' else "0"
    press(value, status = "del")
    
def timeconverter(value, _from = "minute", _to = "hour"):
    result = 0
    if _from == "hour":
        if _to == "minute":
            result = value * 60
        elif _to == "second":
            result = value * 3600
        else:
            result = value
    elif _from == "minute":
        if _to == "hour":
            result = value / 60
        elif _to == "second":
            result = value * 60
        else:
            result = value
    elif _from == "second":
        if _to == "hour":
            result = value / 3600
        elif _to == "minute":
            result = value / 60
        else:
            result = value
    return result
    
    
    
app = Tk()
app.title("Time Converter")

value = '0'
result = 0
b = [[],[],[]]
count = 9
# Create a Tkinter variable
fromvar = StringVar(app)

# Dictionary with options
fromvar.set('Hour') # set the default option

popupMenu = OptionMenu(app, fromvar, *choices, command = lambda x: dropDown(x))
popupMenu.grid(row = 0, column = 0, columnspan = 1, rowspan = 1)

# label = Label(app, text = "Hour")
# label.grid(row = 0, column = 0, columnspan = 1, rowspan = 1)
label_value = Label(app, text = 0, font = 15, height = height, width = width)
label_value.grid(row = 1, column = 0, columnspan = 1, rowspan = 1)


ce_button = button(app, "CE" ,ce) 
ce_button.grid(row = 0, column = 1)


zero_button = button(app, "0" ,press) 
zero_button.grid(row = 0, column = 2)

del_button = button(app, "DEL" ,del_) 
del_button.grid(row = 0, column = 3)
for i in range(3):
    for j in range(3):        
        b[i].append(button(app,count, press))
        b[i][j].grid(row = i + 1, column = j+1)
        count -=1


label_result = Label(app, text = result, font = 15, height = height, width = width)
label_result.grid(row = 2, column = 0, columnspan = 1, rowspan = 2)

# Create a Tkinter variable
tovar = StringVar(app)

# Dictionary with options
tovar.set('Hour') # set the default option

topopMenu = OptionMenu(app, tovar, *choices ,command = lambda x: dropDown(x))
topopMenu.grid(row = 3, column = 0, columnspan = 1, rowspan = 1)

app.mainloop()
