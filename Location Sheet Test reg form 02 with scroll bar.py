from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from tkcalendar import DateEntry
import datetime
import csv
import xml.etree.ElementTree as gfg

root = Tk()
root.geometry('520x960')
root.title("Location Sheet")

#exporting entered data
def save():
    now = datetime.datetime.now()
    #save data in txt file

    s='\n'+now.strftime("%d-%m-%Y %H:%M")+'\t'+e1.get()+'\t'+e2.get()+'\t '+e3.get()+'\t'+ e4.get()+'\t'+e5.get()+'\t '+e6.get()+'\t'+e7.get()+'\t '+e8.get()+'\t'+ e9.get()+'\t'+e10.get()+'\t '+e11.get()+'\t'+e12.get()+'\t '+e13.get()+'\t'+ e14.get()+'\t'+e15.get()+'\t '+e16.get()+'\t'+e17.get()+'\t '+e18.get()+'\t'+ e19.get()+'\t'+e20.get()+'\t '+e21.get()+'\t'+ e22.get()+'\t'+ e23.get()
    f = open(('locationdetails.txt'), 'a')
    f.write(s)
    f.close()
    
    #save data in csv file
    with open('LocationFile.csv', 'a') as fs:
        w = csv.writer(fs, dialect='excel-tab')
        w.writerow([now.strftime("%d-%m-%Y %H:%M"), e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get(),e12.get(),e13.get(),e14.get(),e15.get(),e16.get(),e17.get(),e18.get(),e19.get(),e20.get(),e21.get(),e22.get(),e23.get()])
        fs.close()
        
def saveinfo():
    save()        


#function to generate the XML file
def GenerateXML(fileName) :
    
    root = gfg.Element("Settings")
    
    m1 = gfg.Element("Location")
    root.append (m1)
      
    b1 = gfg.SubElement(m1, "Location_name")
    b1.text = e1.get()
    b2 = gfg.SubElement(m1, "Type_of_climate")
    b2.text = e2.get()
    b3 = gfg.SubElement(m1, "Type_of_nature")
    b3.text = e3.get()
    b4 = gfg.SubElement(m1, "Land_area_size")
    b4.text = e4.get()
      
    m2 = gfg.Element("History")
    root.append (m2)
      
    c1 = gfg.SubElement(m2, "Brief_history")
    c1.text = e5.get()
    c2 = gfg.SubElement(m2, "Proud_milestones")
    c2.text = e6.get()
    c3 = gfg.SubElement(m2, "Historical_trauma")
    c3.text = e7.get()
      
    m3 = gfg.Element("Demographics")
    root.append (m3)
      
    d1 = gfg.SubElement(m3, "Population_No")
    d1.text = e8.get()
    d2 = gfg.SubElement(m3, "Ethnic_groups")
    d2.text = e9.get()
    d3 = gfg.SubElement(m3, "Religions")
    d3.text = e10.get()
    d4 = gfg.SubElement(m3, "Languages")
    d4.text = e11.get()
    
    m4 = gfg.Element("Culture")
    root.append (m4)
      
    f1 = gfg.SubElement(m4, "Arts")
    f1.text = e12.get()
    f2 = gfg.SubElement(m4, "Cuisine")
    f2.text = e13.get()
    f3 = gfg.SubElement(m4, "Media_outlets")
    f3.text = e14.get()
    
    m5= gfg.Element("Politics")
    root.append (m5)
      
    g1 = gfg.SubElement(m5, "Political_system")
    g1.text = e15.get()
    g2 = gfg.SubElement(m5, "Foreign_relations")
    g2.text = e16.get()
    
    m6= gfg.Element("Economy")
    root.append (m6)
      
    h1 = gfg.SubElement(m6, "Economic_status")
    h1.text = e17.get()
    h2 = gfg.SubElement(m6, "Currency")
    h2.text = e18.get()
    h3 = gfg.SubElement(m6, "Main_industries")
    h3.text = e19.get()
    
    m7= gfg.Element("Infrastructure")
    root.append (m7)
      
    i1 = gfg.SubElement(m7, "Infrastructure_status")
    i1.text = e20.get()
    i2 = gfg.SubElement(m7, "Water_availability")
    i2.text = e21.get()
    i3 = gfg.SubElement(m7, "Education_level")
    i3.text = e22.get()
    i4 = gfg.SubElement(m7, "Healthcare_level")
    i4.text = e23.get()
    
    
    
    tree = gfg.ElementTree(root)
    
      
    with open (fileName, "wb") as files :
        tree.write(files)





# Widget frame for scrollbar
widget_frame = Frame(root, bg = "#FFFFFF")
widget_frame.pack(side = "right", fill = Y)

#create a scrollbar for widget frame
scroll_widget = Scrollbar(widget_frame)
scroll_widget.pack(side = RIGHT, fill = Y)


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

#Sub-heading Culture
l16 = Label(root, text="Culture",width=18,font=("times",14,"bold"),fg='black')
l16.place(x=0,y=780)

#Labels Culture
l17 = Label(root, text="Arts",width=20,font=("times",12,"bold"),anchor="w")
l17.place(x=70,y=830)
e12 = Entry(root,width=30,bd=2)
e12.place(x=240,y=830)

l18 = Label(root, text="Cuisine",width=20,font=("times",12,"bold"),anchor="w")
l18.place(x=70,y=880)
e13 = Entry(root,width=30,bd=2)
e13.place(x=240,y=880)

l19 = Label(root, text="Media outlets",width=20,font=("times",12,"bold"),anchor="w")
l19.place(x=70,y=930)
e14 = Entry(root,width=30,bd=2)
e14.place(x=240,y=930)

#Sub-heading Politics
l20 = Label(root, text="Politics",width=18,font=("times",14,"bold"),fg='black')
l20.place(x=0,y=980)

#Labels Politics
l21 = Label(root, text="Political system",width=20,font=("times",12,"bold"),anchor="w")
l21.place(x=70,y=1030)
e15 = Entry(root,width=30,bd=2)
e15.place(x=240,y=1030)

l21 = Label(root, text="Foreign relations",width=20,font=("times",12,"bold"),anchor="w")
l21.place(x=70,y=1080)
e16 = Entry(root,width=30,bd=2)
e16.place(x=240,y=1080)

#Sub-heading Economy
l22 = Label(root, text="Economy",width=18,font=("times",14,"bold"),fg='black')
l22.place(x=0,y=1130)

#Labels Economy
l22 = Label(root, text="Economic status",width=20,font=("times",12,"bold"),anchor="w")
l22.place(x=70,y=1180)
e17 = Entry(root,width=30,bd=2)
e17.place(x=240,y=1180)

l23 = Label(root, text="Currency",width=20,font=("times",12,"bold"),anchor="w")
l23.place(x=70,y=1230)
e18 = Entry(root,width=30,bd=2)
e18.place(x=240,y=1230)

l24 = Label(root, text="Main industries",width=20,font=("times",12,"bold"),anchor="w")
l24.place(x=70,y=1280)
e19 = Entry(root,width=30,bd=2)
e19.place(x=240,y=1280)

#Sub-heading Infrastructure
l25 = Label(root, text="Infrastructure",width=18,font=("times",14,"bold"),fg='black')
l25.place(x=0,y=1330)

#Labels Economy
l26 = Label(root, text="Infrastructure status",width=20,font=("times",12,"bold"),anchor="w")
l26.place(x=70,y=1380)
e20 = Entry(root,width=30,bd=2)
e20.place(x=240,y=1380)

l27 = Label(root, text="Water availability",width=20,font=("times",12,"bold"),anchor="w")
l27.place(x=70,y=1430)
e21 = Entry(root,width=30,bd=2)
e21.place(x=240,y=1430)

l28 = Label(root, text="Education level",width=20,font=("times",12,"bold"),anchor="w")
l28.place(x=70,y=1480)
e22 = Entry(root,width=30,bd=2)
e22.place(x=240,y=1480)

l29 = Label(root, text="Healthcare level",width=20,font=("times",12,"bold"),anchor="w")
l29.place(x=70,y=1530)
e23 = Entry(root,width=30,bd=2)
e23.place(x=240,y=1530)


# submit and cancel buttons
b1 = Button(root, text='Submit',command=saveinfo,width=15,bg='green',fg='white',font=("times",12,"bold"))
b1.place(x=120,y=440)
b2 = Button(root, text='Cancel',command=root.destroy,width=15,bg='maroon',fg='white',font=("times",12,"bold"))
b2.place(x=320,y=440)


# Driver Code for XML
if __name__ == "__main__": 
    GenerateXML("Catalog.xml")


root.mainloop()