import tkinter as tk
from tkinter import ttk
from random import choice, shuffle

def generate_password():
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = lowercase.upper()
    digits = "0123456789"
    special_chars = "!@#$%^&*()_-+=<>?/{}"
    
    all_chars = lowercase + uppercase + digits + special_chars
    
    length = int(length_var.get())
    
    if length < 7:
        result_label.config(text="Password length must be at least 6 characters.")
    else:
        password_list = [choice(lowercase), choice(uppercase), choice(digits), choice(special_chars)]
        remaining_length = length - len(password_list)
        password_list.extend([choice(all_chars) for _ in range(remaining_length)])
        shuffle(password_list)
        password = ''.join(password_list)
        result_label.config(text=f"Generated Password: {password}")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and configure the main frame
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

# Create widgets
length_label = ttk.Label(frame, text="Password Length:")
length_label.grid(row=0, column=0, sticky=tk.W)

length_var = tk.StringVar(value="10")  # Default length
length_entry = ttk.Entry(frame, textvariable=length_var)
length_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

generate_button = ttk.Button(frame, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, pady=20)

result_label = ttk.Label(frame, text="")
result_label.grid(row=2, column=0, columnspan=2)

# Start the main event loop
root.mainloop()
