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