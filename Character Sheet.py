from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from tkcalendar import DateEntry
import datetime
import csv
import xml.etree.ElementTree as gfg

root = Tk()
root.geometry('520x900+900+85')
root.title("Character Sheet")

#exporting entered data
def save():
    """saves the input data in txt and csv file"""
    now = datetime.datetime.now()
    #save data in txt file

    s="Full name: "+e1.get()+'\n'+"Nickname: "+e2.get()+'\n'+"Birthdate: " +e3.get()+'\n'+"Age: " + e4.get()+'\n'+"Weight: " +e5.get()+'\n'+"Height: " +e6.get()+'\n'+"Good personality traits: " +e7.get()+'\n'+"Bad personality traits: "+e8.get()
    f = open(("char_"+e1.get()+".txt"), "w")
    f.write(s)
    f.close()
    root.destroy()
        
def saveinfo():
    save()
    root.destroy
    
    
# Widget frame for scrollbar
widget_frame = Frame(root, bg = "#FFFFFF")
widget_frame.pack(side = "right", fill = Y)

#create a scrollbar for widget frame
scroll_widget = Scrollbar(widget_frame)
scroll_widget.pack(side = RIGHT, fill = Y)

#scroll_widget.config(command = widget_frame.yview)


#Heading
l1 = Label(root, text="Character form",width=25,font=("times",20,"bold"),fg='black')
l1.place(x=70,y=50)

#Sub-heading Character Chart
l2 = Label(root, text="Character Chart",width=20,font=("times",14,"bold"),fg='black')
l2.place(x=22,y=100)

#Labels Location Chart
l3 = Label(root, text="Full name",width=20,font=("times",12,"bold"),anchor="w")
l3.place(x=70,y=130)
e1 = Entry(root,width=30,bd=2)
e1.place(x=240,y=130)

l4 = Label(root, text="Nickname",width=20,font=("times",12,"bold"),anchor="w")
l4.place(x=70,y=180)
e2 = Entry(root,width=30,bd=2)
e2.place(x=240,y=180)

l5 = Label(root, text="Birthdate",width=20,font=("times",12,"bold"),anchor="w")
l5.place(x=70,y=230)
e3 = Entry(root,width=30,bd=2)
e3.place(x=240,y=230)

#Sub-heading Physical appearance
l6 = Label(root, text="Physical appearance",width=18,font=("times",14,"bold"),fg='black')
l6.place(x=0,y=280)

#Labels Physical appearance
l7 = Label(root, text="Age",width=20,font=("times",12,"bold"),anchor="w")
l7.place(x=70,y=330)
e4 = Entry(root,width=30,bd=2)
e4.place(x=240,y=330)

l8 = Label(root, text="Weight",width=20,font=("times",12,"bold"),anchor="w")
l8.place(x=70,y=380)
e5 = Entry(root,width=30,bd=2)
e5.place(x=240,y=380)

l9 = Label(root, text="Height",width=20,font=("times",12,"bold"),anchor="w")
l9.place(x=70,y=430)
e6 = Entry(root,width=30,bd=2)
e6.place(x=240,y=430)

#Sub-heading Personality
l10 = Label(root, text="Personality",width=18,font=("times",14,"bold"),fg='black')
l10.place(x=0,y=480)

#Labels Personality
l11 = Label(root, text="Good personality traits",width=20,font=("times",12,"bold"),anchor="w")
l11.place(x=70,y=530)
e7 = Entry(root,width=30,bd=2)
e7.place(x=240,y=530)

l12 = Label(root, text="Bad personality traits",width=20,font=("times",12,"bold"),anchor="w")
l12.place(x=70,y=580)
e8 = Entry(root,width=30,bd=2)
e8.place(x=240,y=580)


# submit and cancel buttons
b1 = Button(root, text='Submit',command=saveinfo,width=15,bg='#93c47d',fg='white',font=("times",12,"bold"))
b1.place(x=80,y=10)
b2 = Button(root, text='Cancel',command=root.destroy,width=15,bg='#e06666',fg='white',font=("times",12,"bold"))
b2.place(x=280,y=10)

root.mainloop()