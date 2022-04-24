def copy_text(shortcut):
    global copied_text
    
    if shortcut:
        copied_text = root.clipboard_get()
        
    if text_box.selection_get():
        copied_text = text_box.selection_get()
        root.clipboard_clear()
        root.clipboard_append(copied_text)

def paste_text(shortcut):
    global copied_text
    
    if shortcut:
        copied_text = root.clipboard_get()
    else:
        if copied_text:
            cursor = text_box.index(INSERT)
            text_box.insert(cursor, copied_text)

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
