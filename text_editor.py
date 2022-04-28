from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import font
from file_actions import *
import os
import subprocess

window = Tk()
window.title("Bookster")
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry('%dx%d+%d+%d' % (w, h-95, 0, 0))
window.configure(bg = "#f2f0f7")
#window.attributes("-fullscreen", True)

global copied_text
copied_text = False

# Function to open a file
def open_file():
    """Function that clears text box and displays contents of a newly chosen file. Default directory for files is set to Documents folder."""
    text_box.delete(1.0, END)
    
    text_file = filedialog.askopenfilename(initialdir="Documents")
        
    name = os.path.basename(text_file)
    window.title(name + " - Bookster")
    
    
    text_file = open(text_file, 'r')
    read_file = text_file.read()
    
    text_box.insert(END, read_file)
    text_file.close


# Function to create new file
def create_file():
    """Function to create a new file. It clears existing text from the text box."""
    text_box.delete(1.0, END)
    window.title("New file - Bookster")

# Copy function
def copy_text(shortcut):
    """Function that allows copying selected text."""
    
    # If user uses windows shortcuts - get copied text from the clipboard
    if shortcut:
        copied_text = window.clipboard_get()
        
    if text_box.selection_get():
        copied_text = text_box.selection_get()
        window.clipboard_clear()
        window.clipboard_append(copied_text)

# Paste function
def paste_text(shortcut):
    """Function that allows pasting selected text."""
    
    # If user uses windows shortcuts - get copied text from the clipboard
    if shortcut:
        copied_text = window.clipboard_get()
    else:
        if copied_text:
            cursor = text_box.index(INSERT)
            text_box.insert(cursor, copied_text)

# Cut function
def cut_text(shortcut):
    """Function that allows cutting selected text."""
    
    # If user uses windows shortcuts - get copied text from the clipboard
    if shortcut:
        copied_text = window.clipboard_get()
    else:
            
        if text_box.selection_get():
            copied_text = text_box.selection_get()
            text_box.delete("sel.first", "sel.last")
            window.clipboard_clear()
            window.clipboard_append(copied_text)
            
# Function for printing a text file on a printer - WIP            
def print_file():
    pass

# Make text bold
def bold_text():
    """Function that makes selected text bold or removes bold weight if the text was already bold."""
    bold_text = font.Font(text_box, text_box.cget("font"))
    bold_text.configure(weight = "bold")
    
    text_box.tag_configure("bold", font = bold_text)
    
    current_tags = text_box.tag_names("sel.first")
    
    if "bold" in current_tags:
        text_box.tag_remove("bold", "sel.first", "sel.last")
    else:
        text_box.tag_add("bold", "sel.first", "sel.last")

# Make text italic
def italic_text():
    """Function that makes selected text italic or removes italic slant if the text was already italic."""
    italic_text = font.Font(text_box, text_box.cget("font"))
    italic_text.configure(slant = "italic")
    
    text_box.tag_configure("italic", font = italic_text)
    
    current_tags = text_box.tag_names("sel.first")
    
    if "italic" in current_tags:
        text_box.tag_remove("italic", "sel.first", "sel.last")
    else:
        text_box.tag_add("italic", "sel.first", "sel.last")

# Underline text
def underscore_text():
    """Function that makes selected text underlined or removes it if the text was already underlined."""
    underline_text = font.Font(text_box, text_box.cget("font"))
    underline_text.configure(underline = 1)
    
    text_box.tag_configure("underline", font = underline_text)
    
    current_tags = text_box.tag_names("sel.first")
    
    if "underline" in current_tags:
        text_box.tag_remove("underline", "sel.first", "sel.last")
    else:
        text_box.tag_add("underline", "sel.first", "sel.last")
        
# WIP Function that executes upon New Character button press
def new_character():
    pass

# Function that executes upon New Location button press
def new_location():
    """Function that calls Location_sheet script upon button press."""
    subprocess.call(["python", "Location_sheet.py"])
    


# Toolbar
tools_frame = Frame(window, bg = "#d9d2e9")
tools_frame.pack(fill = X, pady = 5)

# Textbox frame
text_frame = Frame(window, width = 2480, height = h - 400, pady = 10)
text_frame.place(x = 30, y = 30)

# Widget frame
widget_frame = Frame(window, width = 2480, padx = 50, pady = 50)
widget_frame.place(x = 870, y = 30)

#Scrollbar for text
scroll_bar = Scrollbar(text_frame)
scroll_bar.pack(side = RIGHT, fill = Y)

# Text box
text_box = Text(text_frame, width = 90, height = 55, font = ("Helvetica", 12),
                selectbackground = "#FCF5E2", selectforeground = "black",
                undo = True, yscrollcommand = scroll_bar.set)
text_box.pack(pady = 5)

scroll_bar.config(command = text_box.yview)

# Text box for reading files

right_scrollbar = Scrollbar(text_frame)
right_scrollbar.pack(side = RIGHT, fill = Y)

read_box = Text(widget_frame, width = 90, height = 40, font = ("Helvetica", 12),
                selectbackground = "#FCF5E2", selectforeground = "black",
                undo = True, yscrollcommand = right_scrollbar.set)
read_box.pack()

read_box.config(state=DISABLED)

right_scrollbar.config(command = read_box.yview)

#scroll_widget.config(command = widget_frame.yview)

# Widget side
character_button = Button(widget_frame, text = "New character", command = new_character)
character_button.pack(padx = 5, pady = 5)

location_button = Button(widget_frame, text = "New Location", command = new_location, padx = 3)
location_button.pack(padx = 5, pady = 5)

# Menu
menu_tab = Menu(window)
window.config(menu = menu_tab)

# File
file_menu = Menu(menu_tab, tearoff = False)
menu_tab.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "New", command = create_file)
file_menu.add_command(label = "Open", command = open_file)
file_menu.add_command(label = "Save text file", command = save_file)
file_menu.add_command(label = "Save as", command = save_file_as)
file_menu.add_command(label = "Print", command = print_file)
file_menu.add_command(label = "Exit", command = window.destroy)

# Edit
edit_menu = Menu(menu_tab, tearoff = False)
menu_tab.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Copy    Ctrl+C", command =  lambda: copy_text(False))
edit_menu.add_command(label = "Paste   Ctrl+V", command = lambda: paste_text(False))
edit_menu.add_command(label = "Cut    Ctrl+X", command = lambda: cut_text(False))
edit_menu.add_command(label = "Undo   Ctrl+Z")
edit_menu.add_command(label = "Redo   Ctrl+Y")

# Status bar
written = 10000 #placeholder value until functions are ready
goal = 20000 #placeholder value until functions are ready
status_bar = Label(window, bg = "#d9d2e9", text = f"Writing goal {written}/{goal} {written/goal*100}%", anchor = S)
status_bar.pack(fill = X, side = BOTTOM)

# Toolbar buttons and widgets
bold = Button(tools_frame, text = "  B  ", command = bold_text)
bold.grid(row = 0, column = 0, padx = 5, sticky = W)

italic = Button(tools_frame, text = "  I  ", command = italic_text)
italic.grid(row = 0, column = 2, padx = 5)

underscore = Button(tools_frame, text = "  U  ", command = underscore_text)
underscore.grid(row = 0, column = 4, padx = 5)


# Key bindings for Copy-Paste-Cut-Print-Exit
window.bind("<Control-x>", cut_text)
window.bind("<Control-c>", copy_text)
window.bind("<Control-v>", paste_text)

window.mainloop()


