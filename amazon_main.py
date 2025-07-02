import tkinter as tk
from tkinter import messagebox
from clean_folder import clean_folder
from rename_files import rename_files

bg_color = "#EEE0A2"      
button_color = "#D8BFDF"  
hover_color = "#C5A6CC"   
text_color = "#4B2E53"    
title_color = "#7A517D"   


def run_clean_folder():
    try:
        clean_folder()
        messagebox.showinfo("Success", "Folder cleaned successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while cleaning:\n{e}")

def run_rename_files():
    try:
        rename_files()
        messagebox.showinfo("Success", "Files renamed successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while renaming:\n{e}")

# main window
root = tk.Tk()
root.title("Amazon_Toffee Lion")
root.geometry("360x230")
root.configure(bg=bg_color)

# title label
title_label = tk.Label(
    root,
    text="Amazon_Toffee Lion",
    bg=bg_color,
    fg=title_color,
    font=("Helvetica", 18, "bold")
)
title_label.pack(pady=(20, 10))

# hover
def on_enter(e, btn):
    btn.config(bg=hover_color)

def on_leave(e, btn):
    btn.config(bg=button_color)

# create btn
def create_button(text, command):
    btn = tk.Button(
        root,
        text=text,
        command=command,
        bg=button_color,
        fg=text_color,
        font=("Helvetica", 12, "bold"),
        relief="flat",
        activebackground=hover_color,
        width=25,
        height=2,
        cursor="hand2"
    )
    btn.pack(pady=10)
    btn.bind("<Enter>", lambda e: on_enter(e, btn))
    btn.bind("<Leave>", lambda e: on_leave(e, btn))
    return btn

# add btn
create_button("Clean Folders", run_clean_folder)
create_button("Rename Files", run_rename_files)


root.mainloop()
