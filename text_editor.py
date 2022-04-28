from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import font
import os
import subprocess

window = Tk()
window.title("Bookster")
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry('%dx%d+%d+%d' % (w, h-95, 0, 0))
window.configure(bg = "#f2f0f7")

global copied_text
copied_text = False

global if_open_file
if_open_file = False

global open_name
open_name = False

# Function to open a file
def open_file():
    """Function that clears text box and displays contents of a newly chosen file. Default directory for files is set to Documents folder."""  
   
    text_box.delete(1.0, END)
        
    text_file = filedialog.askopenfilename(initialdir="Documents", title = "Open file")
    
    if text_file:
        global open_name
        open_name = text_file
    
    name = os.path.basename(text_file)
    window.title(name + " - Bookster")
       
    text_file = open(text_file, 'r')
    read_file = text_file.read()
        
    text_box.insert(END, read_file)
    text_file.close


# Function to create new file
def create_file():
    """Function to create a new file. It clears existing text from the text box."""
    try:
        text_box.delete(1.0, END)
        window.title("New file - Bookster")
    except:
        pass

# Save file as - currently unfinished
def save_file_as():
    """Function for saving text from the text box to a new file of a chosen format."""
    text_file = filedialog.asksaveasfilename(initialdir="Documents", defaultextension=".txt", title = "Save file")
    
    if text_file:
        name = os.path.basename(text_file)
        window.title(name + " File saved - Bookster")
        
        text_file = open(text_file, 'w')
        text_file.write(text_box.get(1.0, END))
        
        text_file.close
        
# Save file
def save_file():
    """Function for saving text from the text box to a new file. If file is already open - changes are being saved. If nno file open - file is saved as new."""
    global open_name
    
    if  open_name:
        text_file = open(open_name, 'w')
        text_file.write(text_box.get(1.0, END))
        
        text_file.close
    else:
        save_file_as()
    
    
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
    """Function to print text file on a printer"""
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
    """Function that calls Character_sheet script upon button press."""
    subprocess.call(["python", "Character Sheet.py"])

# Function that executes upon New Location button press
def new_location():
    """Function that calls Location_sheet script upon button press."""
    subprocess.call(["python", "Location_sheet.py"])
    
# Display character information
def display_char(event):
    """Function displays contents of chosen character file on a screen"""
    
    read_box.config(state=NORMAL) 
    read_box.delete(1.0, END)         
    
    read_file = open("char_"+clicked_char.get()+".txt", "r").read()   
    read_box.insert(END, read_file)
    
    read_box.config(state=DISABLED)

# Display location information
def display_loc(event):
    """Function displays contents of chosen location file on a screen"""
    
    read_box.config(state=NORMAL)   
    read_box.delete(1.0, END)         
    
    read_file = open("loc_"+clicked_loc.get()+".txt", "r").read() 
    read_box.insert(END, read_file)
    
    read_box.config(state=DISABLED)    

# WIP Function to refresh list of existing files
def refresh_frame():
    """Function to refresh list of existing files to dynamically access newly created ones"""
    pass    

# WIP Function to count words in a  file
    """Function to calculate total amount of typed words in the text file"""
def get_words(current_file):
    try:
        file = open(current_file, "r")
        read_words = file.read()
        per_word = read_words.split()   
        total_words = len(per_word)
        
        return total_words
    
    except:
        pass

# Toolbar
tools_frame = Frame(window, bg = "#d9d2e9")
tools_frame.pack(fill = X, pady = 5)

# Textbox frame
text_frame = Frame(window, width = 2480, height = h - 400, pady = 10, bg = "#f2f0f7")
text_frame.place(x = 30, y = 32)

# Widget frame
widget_frame = Frame(window, width = 3020, height = 1600, padx = 10, pady = 10, bg = "#f2f0f7")
widget_frame.place(x = 861, y = 32)

#Scrollbar for text
scroll_bar = Scrollbar(text_frame)
scroll_bar.pack(side = RIGHT, fill = Y)

# Frame for reading box
read_frame = Frame(window, width = 2480, height = h - 400, pady = 10, bg = "#f2f0f7")
read_frame.place(x = 970, y = 32)

# Text box
text_box = Text(text_frame, width = 90, height = 55, font = ("Helvetica", 12),
                selectbackground = "#FCF5E2", selectforeground = "black",
                undo = True, yscrollcommand = scroll_bar.set)
text_box.pack(pady = 5)

scroll_bar.config(command = text_box.yview)

# Text box for reading files

right_scrollbar = Scrollbar(text_frame)
right_scrollbar.pack(side = RIGHT, fill = Y)

read_box = Text(read_frame, width = 90, height = 40, font = ("Helvetica", 12),
                selectbackground = "#FCF5E2", selectforeground = "black",
                undo = True, yscrollcommand = right_scrollbar.set)
read_box.pack()

right_scrollbar.config(command = read_box.yview)

# Dropboxes for character and location selection

characters = []
locations = []
directory = os.getcwd()

clicked_char = StringVar()
clicked_loc = StringVar()

'''Potentially need to separate following into a function. Gets list of character and location files and adds them to the dropdown menu'''
for file in os.listdir(directory):
    if file.endswith(".txt") and file.startswith("char_"):
        char_name = file.strip("char_").strip(".txt")
        characters.append(char_name)
        clicked_char.set(char_name)

for file in os.listdir(directory):
    if file.endswith(".txt") and file.startswith("loc_"):
        loc_name = file.strip("loc_").strip(".txt")
        locations.append(loc_name)
        clicked_loc.set(loc_name)

# Placing elements at the bottom of the read box
char_label = Label(text = "Character: ", bg = "#f2f0f7")
character_dropbox = OptionMenu(widget_frame, clicked_char, *characters, command = display_char)
loc_label = Label(text = "Location: ", bg = "#f2f0f7")
loc_dropbox = OptionMenu(widget_frame, clicked_loc, *locations, command = display_loc)

character_dropbox.place(x = 100, y = 760)
loc_dropbox.place(x = 100, y = 790)

char_label.place(x = 900, y = 810)
loc_label.place(x = 900, y = 840)

# Widget side
character_button = Button(widget_frame, text = "New character", command = new_character, bg = "#d9d2e9")
character_button.place(x = 0, y = 20)

location_button = Button(widget_frame, text = "New Location", command = new_location, padx = 3, bg = "#d9d2e9")
location_button.place(x = 0, y = 60)

refresh_button = Button(widget_frame, text = "Refresh", command = refresh_frame, bg = "#d9d2e9")
refresh_button.place(x = 30, y = 732)

# Menu
menu_tab = Menu(window)
window.config(menu = menu_tab)

# File
file_menu = Menu(menu_tab, tearoff = False)
menu_tab.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "New", command = create_file)
file_menu.add_command(label = "Open", command = open_file)
file_menu.add_command(label = "Save", command = save_file)
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
written = 10000 # placeholder value until function is ready
goal = 20000 # placeholder value until function is ready
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


