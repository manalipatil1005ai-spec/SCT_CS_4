import tkinter as tk
from datetime import datetime

# File to store logs
LOG_FILE = "typed_text_log.txt"

def log_key(event):
    """Log keys typed inside the text box to a file with a timestamp."""
    key = event.char if event.char else f"[{event.keysym}]"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {key}\n")

# GUI setup
root = tk.Tk()
root.title("Typing Logger Demo")
root.geometry("400x200")

label = tk.Label(root, text="Type here (this will be logged inside this app only):", font=("Arial", 12))
label.pack(pady=10)

text_box = tk.Text(root, width=40, height=5, font=("Arial", 12))
text_box.pack()
text_box.bind("<Key>", log_key)

root.mainloop()
