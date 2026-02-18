import tkinter as tk
import re

def check_strength():
    password = entry.get()
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score <= 2:
        result.config(text="Weak Password", fg="red")
    elif score <= 4:
        result.config(text="Medium Password", fg="orange")
    else:
        result.config(text="Strong Password", fg="green")

# Window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("350x200")

# Title
title = tk.Label(root, text="Password Strength Checker", font=("Arial", 14, "bold"))
title.pack(pady=10)

# Entry box
entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=10)

def toggle_password():
    if entry.cget('show') == '*':
        entry.config(show='')
    else:
        entry.config(show='*')

show_btn = tk.Button(root, text="Show/Hide Password", command=toggle_password)
show_btn.pack()


# Button
check_btn = tk.Button(root, text="Check Strength", command=check_strength)
check_btn.pack(pady=10)

root.title("Password Strength Checker")
root.title("Cyber Security Password Analyzer")


# Result
result = tk.Label(root, text="", font=("Arial", 12))
result.pack(pady=10)

root.mainloop()
