from tkinter import *
import os

root = Tk()
root.title("Bookster")
#w, h = root.winfo_screenwidth(), root.winfo_screenheight()
#root.geometry("%dx%d+0+0" % (w, h))
root.geometry("1200x700+200+150")

global if_open_file
if_open_file = False

global copied_text
copied_text = False

# Function to create new file
def create_file():
    text_box.delete(1.0, END)
    root.title("New file - Bookster")
    
    global if_open_file
    if_open_file = False

# Open a file
def open_file():
    text_box.delete(1.0, END)
    
    text_file = filedialog.askopenfilename(initialdir="Documents")
    
    #Check if some file is open
    if text_file:
        global if_open_file
        if_open_file = text_file
        
    name = os.path.basename(text_file)
    root.title(name + " - Bookster")
    
    
    text_file = open(text_file, 'r')
    read_file = text_file.read()
    
    text_box.insert(END, read_file)
    text_file.close

# Save file
def save_file():
    global if_open_file
    
    if  if_open_file:
        text_file = open(if_open_file, 'w')
        text_file.write(text_box.get(1.0, END))
        #root.title(name + " File saved - Bookster")
        
        text_file.close
    else:
        save_file_as()
    
 
# Save file as
def save_file_as():
    text_file = filedialog.asksaveasfilename(initialdir="Documents", defaultextension=".txt", title = "Save file")
    
    if text_file:
        name = os.path.basename(text_file)
        root.title(name + " File saved - Bookster")
        
        text_file = open(text_file, 'w')
        text_file.write(text_box(1.0, END))
        
        text_file.close

# Copy function
def copy_text(shortcut):
    global copied_text
    
    if shortcut:
        copied_text = root.clipboard_get()
        
    if text_box.selection_get():
        copied_text = text_box.selection_get()
        root.clipboard_clear()
        root.clipboard_append(copied_text)

# Paste function
def paste_text(shortcut):
    global copied_text
    
    if shortcut:
        copied_text = root.clipboard_get()
    else:
        if copied_text:
            cursor = text_box.index(INSERT)
            text_box.insert(cursor, copied_text)

# Cut function
def cut_text(shortcut):
    global copied_text
    
    if shortcut:
        copied_text = root.clipboard_get()
    else:
            
        if text_box.selection_get():
            copied_text = text_box.selection_get()
            text_box.delete("sel.first", "sel.last")
            root.clipboard_clear()
            root.clipboard_append(copied_text)

# Make text bold
def bold_text():
    return

# Make text italic
def italic_text():
    return

# Underline text
def underscore_text():
    return

# Toolbar
tools_frame = Frame(root, bg = "#FCF5E2")
tools_frame.pack(fill = X)

# Textbox frame
text_frame = Frame(root)
text_frame.place(x = 30, y = 30)

# Widget frame
widget_frame = Frame(root, bg = "#FFFFFF")
widget_frame.pack(side = "right", fill = Y)

#Scrollbar for text
scroll_bar = Scrollbar(text_frame)
scroll_bar.pack(side = RIGHT, fill = Y)

#Scrollbar for widget frame
scroll_widget = Scrollbar(widget_frame)
scroll_widget.pack(side = RIGHT, fill = Y)

# Text box
text_box = Text(text_frame, width = 90, height = 55, font = ("Helvetica", 12),
                selectbackground = "#FCF5E2", selectforeground = "black",
                undo = True, yscrollcommand = scroll_bar.set)
text_box.pack(pady = 5)

scroll_bar.config(command = text_box.yview)

# Menu
menu_tab = Menu(root)
root.config(menu = menu_tab)

# File
file_menu = Menu(menu_tab, tearoff = False)
menu_tab.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "New", command = create_file)
file_menu.add_command(label = "Open", command = open_file)
file_menu.add_command(label = "Save", command = save_file)
file_menu.add_command(label = "Save as", command = save_file_as)
file_menu.add_command(label = "Print")
file_menu.add_command(label = "Exit", command = root.destroy)

# Edit
edit_menu = Menu(menu_tab, tearoff = False)
menu_tab.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Copy    Ctrl+C", command =  lambda: copy_text(False))
edit_menu.add_command(label = "Paste   Ctrl+V", command = lambda: paste_text(False))
edit_menu.add_command(label = "Cut    Ctrl+X", command = lambda: cut_text(False))
edit_menu.add_command(label = "Undo   Ctrl+Z")
edit_menu.add_command(label = "Redo   Ctrl+Y")

# Status bar
status_bar = Label(root, text = f"Writing goal 5000/10000 50%", anchor = S)
status_bar.pack(fill = X, side = BOTTOM, ipady = 5)

# Toolbar buttons and widgets
bold = Button(tools_frame, text = "  B  ", command = bold_text)
bold.grid(row = 0, column = 0, padx = 5, sticky = W)

italic = Button(tools_frame, text = "  I  ", command = italic_text)
italic.grid(row = 0, column = 2, padx = 5)

underscore = Button(tools_frame, text = "  U  ", command = underscore_text)
underscore.grid(row = 0, column = 4, padx = 5)


# Key bindings for Copy-Paste-Cut-Print-Exit
root.bind("<Control-x>", cut_text)
root.bind("<Control-c>", copy_text)
root.bind("<Control-v>", paste_text)

root.mainloop()
