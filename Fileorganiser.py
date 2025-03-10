import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
#function for sorting files
def organize_files():
    path = entry.get()
    if not os.path.isdir(path):
        messagebox.showerror("Error", "Invalid Directory!")
        return
    
    files = os.listdir(path)
    for file in files:
        filename, extension = os.path.splitext(file)
        extension = extension[1:] 
        
        if extension:  s
            ext_path = os.path.join(path, extension)
            if not os.path.exists(ext_path):
                os.makedirs(ext_path)
            shutil.move(os.path.join(path, file), os.path.join(ext_path, file))
    
    messagebox.showinfo("Success", "Files Organized Successfully!")

def browse_directory():
    folder_selected = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, folder_selected)

# Creating GUI window
root = tk.Tk()
root.title("File Organizer")
root.geometry("400x200")

# Adding UI Elements
label = tk.Label(root, text="Select Directory:")
label.pack(pady=5)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

browse_button = tk.Button(root, text="Browse", command=browse_directory)
browse_button.pack(pady=5)

organize_button = tk.Button(root, text="Organize Files", command=organize_files)
organize_button.pack(pady=10)

# Run This GUI loop
root.mainloop()
