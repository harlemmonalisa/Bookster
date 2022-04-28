from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from tkcalendar import DateEntry
import datetime
import csv
import xml.etree.ElementTree as gfg

root = Tk()
root.geometry('520x900+900+85')
root.title("Location Sheet")

#exporting entered data
def save():
    now = datetime.datetime.now()
    #save data in txt file

    s="Location name: "+e1.get()+'\n'+"Type of climate: "+e2.get()+'\n'+"Type of nature: "+e3.get()+'\n'+"Land area size: " +e4.get()+'\n'+"Brief history: " +e5.get()+'\n' "Proud milestones: " +e6.get()+'\n'+"Historical trauma: " +e7.get()+'\n'+"Population No.: " +e8.get()+'\n'+"Ethnic groups: " +e9.get()+'\n'+"Religions: " +e10.get()+'\n'+ "Languages: " +e11.get()
    f = open(("loc_"+e1.get()+".txt"), "w")
    f.write(s)
    f.close()
    root.destroy()
    
        
def saveinfo():
    save()        


# Widget frame for scrollbar
widget_frame = Frame(root, bg = "#FFFFFF")
widget_frame.pack(side = "right", fill = Y)

#create a scrollbar for widget frame
scroll_widget = Scrollbar(widget_frame)
scroll_widget.pack(side = RIGHT, fill = Y)

#scroll_widget.config(command = widget_frame.yview)

#Heading
l1 = Label(root, text="Location form",width=25,font=("times",20,"bold"),fg='black')
l1.place(x=70,y=50)

#Sub-heading Location Chart
l2 = Label(root, text="Location Chart",width=20,font=("times",14,"bold"),fg='black')
l2.place(x=22,y=100)

#Labels Location Chart
l3 = Label(root, text="Location name",width=20,font=("times",12,"bold"),anchor="w")
l3.place(x=70,y=130)
e1 = Entry(root,width=30,bd=2)
e1.place(x=240,y=130)

l4 = Label(root, text="Type of climate",width=20,font=("times",12,"bold"),anchor="w")
l4.place(x=70,y=180)
e2 = Entry(root,width=30,bd=2)
e2.place(x=240,y=180)

l5 = Label(root, text="Type of nature",width=20,font=("times",12,"bold"),anchor="w")
l5.place(x=70,y=230)
e3 = Entry(root,width=30,bd=2)
e3.place(x=240,y=230)

l6 = Label(root, text="Land area size",width=20,font=("times",12,"bold"),anchor="w")
l6.place(x=70,y=280)
e4 = Entry(root,width=30,bd=2)
e4.place(x=240,y=280)

#Sub-heading History
l7 = Label(root, text="History",width=18,font=("times",14,"bold"),fg='black')
l7.place(x=0,y=330)

#Labels History
l8 = Label(root, text="Brief history",width=20,font=("times",12,"bold"),anchor="w")
l8.place(x=70,y=380)
e5 = Entry(root,width=30,bd=2)
e5.place(x=240,y=380)

l9 = Label(root, text="Proud milestones",width=20,font=("times",12,"bold"),anchor="w")
l9.place(x=70,y=430)
e6 = Entry(root,width=30,bd=2)
e6.place(x=240,y=430)

l10 = Label(root, text="Historical trauma",width=20,font=("times",12,"bold"),anchor="w")
l10.place(x=70,y=480)
e7 = Entry(root,width=30,bd=2)
e7.place(x=240,y=480)

#Sub-heading Demographics
l11 = Label(root, text="Demographics",width=23,font=("times",14,"bold"),fg='black')
l11.place(x=0,y=530)

#Labels Demographics
l12 = Label(root, text="Population No.",width=20,font=("times",12,"bold"),anchor="w")
l12.place(x=70,y=580)
e8 = Entry(root,width=30,bd=2)
e8.place(x=240,y=580)

l13 = Label(root, text="Ethnic groups",width=20,font=("times",12,"bold"),anchor="w")
l13.place(x=70,y=630)
e9 = Entry(root,width=30,bd=2)
e9.place(x=240,y=630)

l14 = Label(root, text="Religions",width=20,font=("times",12,"bold"),anchor="w")
l14.place(x=70,y=680)
e10 = Entry(root,width=30,bd=2)
e10.place(x=240,y=680)

l15 = Label(root, text="Languages",width=20,font=("times",12,"bold"),anchor="w")
l15.place(x=70,y=730)
e11 = Entry(root,width=30,bd=2)
e11.place(x=240,y=730)


# submit and cancel buttons
b1 = Button(root, text='Submit',command=saveinfo,width=15,bg='#93c47d',fg='white',font=("times",12,"bold"))
b1.place(x=80,y=10)
b2 = Button(root, text='Cancel',command=root.destroy,width=15,bg='#e06666',fg='white',font=("times",12,"bold"))
b2.place(x=280,y=10)


root.mainloop()