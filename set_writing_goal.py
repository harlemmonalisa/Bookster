import tkinter as tk
from tkinter import *
import datetime

window = tk.Tk()
window.geometry('320x150+500+85')
window.title("Set writing goal")

#exporting entered data
def save():
    now = datetime.datetime.now()
    #save data in txt file

    s= entry.get()
    f = open(("target.txt"), "w")
    f.write(s)
    f.close()
    window.destroy()
            
def saveinfo():
    save()

#label and entry box
label = tk.Label(text="Insert your target word count")
entry = tk.Entry()

label.pack()
entry.pack()
    

# submit and cancel buttons
b1 = Button(window, text='Submit',command=saveinfo,width=15,bg='#93c47d',fg='white',font=("times",12,"bold"))
b1.place(x=85,y=50)

window.mainloop()