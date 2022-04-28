from tkinter import filedialog

global if_open_file
if_open_file = False

# Save file
def save_file():
    """Function for saving text from the text box to a new file. If file is already open - changes are being saved. If nno file open - file is saved as new."""
    if  if_open_file:
        text_file = open(if_open_file, 'w')
        text_file.write(text_box.get(1.0, END))
        
        text_file.close
    else:
        save_file_as()
    
 
# Save file as - currently unfinished
def save_file_as():
    """Function for saving text from the text box to a new file of a chosen format."""
    text_file = filedialog.asksaveasfilename(initialdir="Documents", defaultextension=".txt", title = "Save file")
    
    if text_file:
        name = os.path.basename(text_file)
        window.title(name + " File saved - Bookster")
        
        text_file = open(text_file, 'w')
        text_file.write(text_box(1.0, END))
        
        text_file.close
