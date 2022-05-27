from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import font
from subprocess import Popen
import requests
import random
import os
import subprocess
import datetime
import win32api

window = Tk()
window.title("Bookster")
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry('%dx%d+%d+%d' % (w, h-91, -7, 0))
window.configure(bg = "#FAFDFD")

global copied_text
copied_text = False

global if_open_file
if_open_file = False

global open_name
open_name = False

global characters
global locations
global projects
global name_entry
global name_window
global path
global init_path
global projects_dropbox
global open_project
global file_name

characters = []
locations = []
projects = []

clicked_char = StringVar()
clicked_loc = StringVar()

init_path = os.path.dirname(os.path.realpath(__file__))

# Function to open a file
def open_projects():
    """Function opens a new window with a list ofd exisitng projects and calls display_project(). Default directory for files is set to Documents/Bookster/*Project* folder."""  
    global projects
    global projects_dropbox
    global open_project
    
    open_project = Tk()
    open_project.geometry('320x130+90+95')
    open_project.title("Select project")
    
    projects_label = Label(open_project, text="Select a project to load")
    projects_dropbox = ttk.Combobox(open_project, values = projects, postcommand = get_projects)
    projects_dropbox["state"] = "readonly"
    
    projects_button = Button(open_project, text='Submit', command = display_project, width=15, bg='#93c47d', fg='white', font=("times",12,"bold"))
    
    projects_label.place(x = 10, y = 10)
    projects_dropbox.place(x = 10, y = 30)
    projects_button.place(x = 10, y = 60)
    
def get_projects():
    """Function checks all existing projects and displays them in a list"""
    global projects
    global projects_dropbox
    
    user = os.getlogin()
    directory = "C:/Users/" + user + "/Documents/Bookster"
    
    projects = []
    
    for project in os.listdir(directory):
        project_name = project
        projects.append(project_name)
    projects_dropbox["values"] = projects
  
def display_project():
    """Function dispalys contents of a txt file on the screen, calculates the amount of words written and checks for the word target.
        It then displays word progress in the status bar"""
    global file_name
    user = os.getlogin()
    
    open_dir = "C:/Users/" + user + "/Documents/Bookster/" + projects_dropbox.get()
    os.chdir(open_dir)
    
    file_name = projects_dropbox.get() + ".txt"
    
    text_box.delete(1.0, END)
       
    text_file = open(file_name, 'r')
    read_file = text_file.read()
    
    written = len(read_file.split())
    try:
        goal_file = open("target.txt", 'r')
        goal = int(goal_file.read())
    
    except:
        goal = 50000
        
    status_bar.config(text = f"Writing goal {written}/{goal} {round(written/goal*100)}%")
         
    text_box.insert(END, read_file)
    text_file.close
    open_project.destroy()

# Function to create new file
def create_project():
    """Function to create a new project. It opens a new window to specify project name and calls create_dirs()"""
    global name_window
    
    name_window = Tk()
    name_window.geometry('320x130+90+95')
    name_window.title("Create new project")
    
    global name_entry
    
    name_label = Label(name_window, text="What is the name of your project?")
    name_entry = Entry(name_window, width = 47)

    name_label.place(x = 85, y = 10)
    name_entry.place(x = 15, y = 30)
 
    submit_button = Button(name_window, text='Create project', command = create_dirs, width = 15, bg = '#93c47d', fg = 'white', font = ("times", 12, "bold"))
    submit_button.place(x = 85, y = 65)

    name_window.mainloop()
    
    try:
        text_box.delete(1.0, END)
        name_window.title("New project - Bookster")
           
    except:
        pass
    
def create_dirs():
    """Function creates folders and files for a specified project name"""
    global path
    global project_name
    
    project_name = name_entry.get()
    
    if not project_name:
        error_label = Label(name_window, text="Name cannot be empty!")
        error_label.place(x = 88, y = 98)
        
    else:
        project_name = name_entry.get()
        name_window.destroy()
        user = os.getlogin()
            
        parent_dir = "C:/Users/" + user + "/Documents/Bookster"
        path = os.path.join(parent_dir, project_name)
        
        try:
            os.mkdir(parent_dir)
        except:
            pass
        try:
            os.mkdir(path)
        except:
            pass
        
        os.chdir(path)
        
        text_file = open((project_name+".txt"), "w")
        
# Save file
def save_project():
    """Function for saving changes to the txt file in the project"""
    global file_name
    
    try:
        text_file = open((file_name), "w")
        text_file.write(text_box.get(1.0, END))
        text_file.close
    except:
        pass
       
# Copy function
def copy_text(shortcut):
    """Function that allows copying selected text."""
    global copied_text
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
    global copied_text
    try:
    # If user uses windows shortcuts - get copied text from the clipboard
        if shortcut:
            copied_text = window.clipboard_get()
        else:
            if copied_text:
                cursor = text_box.index(INSERT)
                text_box.insert(cursor, copied_text)
    except:
        pass

# Cut function
def cut_text(shortcut):
    """Function that allows cutting selected text."""
    global copied_text
    # If user uses windows shortcuts - get copied text from the clipboard
    try:
        if shortcut:
            copied_text = window.clipboard_get()
        else:
                
            if text_box.selection_get():
                copied_text = text_box.selection_get()
                text_box.delete("sel.first", "sel.last")
                window.clipboard_clear()
                window.clipboard_append(copied_text)
    except:
        pass
            
# Function for printing a text file on a printer            
def print_file():
    """Function to print text file on a default printer"""
    
    global file_name
    win32api.ShellExecute(0, "print", file_name, None, ".", 0)

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
    global init_path
    
    subprocess.call(["python", init_path +"/Character Sheet.py"])

# Function that executes upon New Location button press
def new_location():
    """Function that calls Location_sheet script upon button press."""
    global init_path

    subprocess.call(["python", init_path + "/Location_sheet.py"])

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
def get_sheets():
    """Function loads created characters and locations into the respective comboboxes"""
    directory = os.getcwd()
    
    characters = []
    locations = []
    for file in os.listdir(directory):
        if file.endswith(".txt") and file.startswith("char_"):
            char_name = file.strip("char_").strip(".txt")
            characters.append(char_name)
            clicked_char.set(char_name)
    character_dropbox["values"] = characters

    for file in os.listdir(directory):
        if file.endswith(".txt") and file.startswith("loc_"):
            loc_name = file.strip("loc_").strip(".txt")
            locations.append(loc_name)
            clicked_loc.set(loc_name)
    loc_dropbox["values"] = locations
    
# WIP Function to count words in a  file
def get_words(current_file):
    """Function to calculate total amount of typed words in the text file"""
    try:
        file = open(current_file, "r")
        read_words = file.read()
        per_word = read_words.split()   
        total_words = len(per_word)
        
        return total_words
    
    except:
        pass
    
def generate_word():
    """Function generates a random word and displays it in the text box"""
    #source where random words will be pulled from
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

    #pulling random words
    response = requests.get(word_site)
    WORDS = response.content.splitlines()

    #execute random word
    random_word = random.choice(WORDS)
    #convert to string type
    string_word = str(random_word)
    #to omit the extra b letter at the front
    final_random_word = string_word[1:]
    
    word_box.config(state=NORMAL)   
    word_box.delete(1.0, END)         
    word_box.insert(END, final_random_word.strip("'"))   
    word_box.config(state=DISABLED)
    
def set_target():
    """Function calls a subprocess to request word target for the project and saves it in the specific file"""
    global init_path
    
    subprocess.call(["python", init_path + "\set_writing_goal.py"])

# Toolbar
tools_frame = Frame(window, bg = "#E4EAEA")
tools_frame.pack(fill = X, pady = 5)

# Textbox frame
text_frame = Frame(window, width = 2480, height = h - 400, pady = 10, bg = "#FAFDFD")
text_frame.place(x = 30, y = 32)

# Widget frame
widget_frame = Frame(window, width = 3020, height = 1600, padx = 10, pady = 10, bg = "#FAFDFD")
widget_frame.place(x = 861, y = 32)

#Scrollbar for text
scroll_bar = Scrollbar(text_frame)
scroll_bar.pack(side = RIGHT, fill = Y)

# Frame for reading box
read_frame = Frame(window, width = 2480, height = h - 400, pady = 10, bg = "#FAFDFD")
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
char_label = Label(text = "Character: ", bg = "#FAFDFD")
character_dropbox = ttk.Combobox(widget_frame, textvariable = clicked_char, values = characters, postcommand = get_sheets)
character_dropbox["state"] = "readonly"
character_dropbox.bind("<<ComboboxSelected>>", display_char)

loc_label = Label(text = "Location: ", bg = "#FAFDFD")
loc_dropbox = ttk.Combobox(widget_frame, textvariable = clicked_loc, values = locations, postcommand = get_sheets)
loc_dropbox["state"] = "readonly"
loc_dropbox.bind("<<ComboboxSelected>>", display_loc)

#Random word field
word_button = Button(widget_frame, text = "Generate random word", command = generate_word, bg = "#E4EAEA")

word_box = Text(widget_frame, width = 20, height = 1, font = ("Helvetica", 12),
                selectbackground = "#FCF5E2", selectforeground = "black",
                undo = True, yscrollcommand = right_scrollbar.set)

# Set writing goal
goal_button = Button(widget_frame, text = "Set writing goal", command = set_target, bg = "#E4EAEA")

# Placing elements at the bottom of the read box
character_dropbox.place(x = 100, y = 760)
loc_dropbox.place(x = 100, y = 790)

char_label.place(x = 900, y = 810)
loc_label.place(x = 900, y = 840)

word_button.place(x = 350, y = 760)
word_box.place(x = 350, y = 790)

goal_button.place(x = 0, y = 160)

# Widget side
character_button = Button(widget_frame, text = "New character", command = new_character, bg = "#E4EAEA")
character_button.place(x = 0, y = 20)

location_button = Button(widget_frame, text = "New Location", command = new_location, padx = 3, bg = "#E4EAEA")
location_button.place(x = 0, y = 60)

# Menu
menu_tab = Menu(window)
window.config(menu = menu_tab)

# File
file_menu = Menu(menu_tab, tearoff = False)
menu_tab.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "Create project", command = create_project)
file_menu.add_command(label = "Open project", command = open_projects)
file_menu.add_command(label = "Save project", command = save_project)
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
status_bar = Label(window, bg = "#E4EAEA", text = f"Open file to see your writing progress", anchor = S)
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
