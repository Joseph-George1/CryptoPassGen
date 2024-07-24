import tkinter as tk
from tkinter import ttk
import string
import random
from datetime import datetime
import os

def submitt():
    length = password_length.get()
    if length and length > 0:
        password1 = Generate_password(length)
        show_output(password1)
    else:
        output_label.config(state=tk.NORMAL)
        output_label.delete(1.0, tk.END)
        output_label.insert(tk.END, "Please enter a valid password length.")
        output_label.config(state=tk.DISABLED)

def Generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

root = tk.Tk()
root.title("Password Generator GUI")
root.geometry("500x400")
root.resizable(False, False)
root.configure(bg='#1e1e1e')

style = ttk.Style()
style.theme_use('clam')
style.configure('TFrame', background='#1e1e1e')
style.configure('TLabel', background='#1e1e1e', foreground='#d3d3d3', font=('Helvetica', 12))
style.configure('TButton', background='#444444', foreground='#ffffff', font=('Helvetica', 12, 'bold'))
style.map('TButton', background=[('active', '#666666')])
style.configure('TEntry', fieldbackground='#333333', foreground='#ffffff', font=('Helvetica', 12))
style.configure('TSeparator', background='#444444')

frame = ttk.Frame(root, padding="20 20 20 20")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

input_label = ttk.Label(frame, text="Enter the name of the app to be saved:")
input_label.grid(row=0, column=0, pady=(0, 10), sticky=tk.W)

user_input = tk.StringVar()
input_entry = ttk.Entry(frame, textvariable=user_input, width=50)
input_entry.grid(row=1, column=0, pady=(0, 20), sticky=tk.W)

password_length_label = ttk.Label(frame, text="Password Length:")
password_length_label.grid(row=2, column=0, pady=(0, 10), sticky=tk.W)

password_length = tk.IntVar()
password_length_entry = ttk.Entry(frame, textvariable=password_length, width=50)
password_length_entry.grid(row=3, column=0, pady=(0, 20), sticky=tk.W)

separator = ttk.Separator(frame, orient='horizontal')
separator.grid(row=4, column=0, pady=(0, 20), sticky=(tk.W, tk.E))

output_frame = ttk.Frame(frame)
output_frame.grid(row=5, column=0, pady=(0, 10), sticky=tk.W)

output_label = tk.Text(output_frame, wrap=tk.WORD, height=4, width=50, font=('Helvetica', 12, 'italic'), bg='#333333', fg='#ffffff')
output_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
output_label.config(state=tk.DISABLED)

scrollbar = ttk.Scrollbar(output_frame, orient=tk.VERTICAL, command=output_label.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
output_label.config(yscrollcommand=scrollbar.set)

def show_output(password):
    output_label.config(state=tk.NORMAL)
    output_label.delete(1.0, tk.END)
    output_label.insert(tk.END, password)
    output_label.config(state=tk.DISABLED)

def copy_output():
    root.clipboard_clear()
    root.clipboard_append(output_label.get(1.0, tk.END).strip())

def save_output():
    password = output_label.get(1.0, tk.END).strip()
    if password:
        file_path = "Password.txt"
        app_name = user_input.get()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write("Password File Created\n")
        with open(file_path, "a") as f:
            f.write(f"New password: {password} - Created on: {timestamp} - For {app_name}\n")
    else:
        output_label.config(state=tk.NORMAL)
        output_label.delete(1.0, tk.END)
        output_label.insert(tk.END, "No password to save.")
        output_label.config(state=tk.DISABLED)

submit_button = ttk.Button(frame, text="Create password", command=submitt)
submit_button.grid(row=6, column=0, pady=(10, 0), sticky=tk.W)

button_frame = ttk.Frame(frame)
button_frame.grid(row=7, column=0, pady=(10, 0), sticky=tk.W)

copy_button = ttk.Button(button_frame, text="Copy Password", command=copy_output)
copy_button.pack(side=tk.LEFT, padx=(0, 10))

save_button = ttk.Button(button_frame, text="Save Password", command=save_output)
save_button.pack(side=tk.LEFT, padx=(10, 0))

for child in frame.winfo_children():
    child.grid_configure(padx=10, pady=5)

root.mainloop()
