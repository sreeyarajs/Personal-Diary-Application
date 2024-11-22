import datetime
import os
import tkinter as tk
from tkinter import messagebox

def create_directory():
    """Creates a directory with the current date as its name."""
    current_date = datetime.date.today()
    directory_name = current_date.strftime('%Y-%m-%d')
    if not os.path.exists(directory_name):
        try:
            os.mkdir(directory_name)
        except OSError as e:
            messagebox.showerror("Error", f"Failed to create directory: {e}")
            return None
    return directory_name

def save_entry():
    """Saves the user's entry in a text file within a date-specific directory."""
    directory_name = create_directory()
    if directory_name is None:
        return  # Abort if directory creation failed.

    current_date_time = datetime.datetime.now()
    file_name = current_date_time.strftime('%Y-%m-%d_%H-%M-%S')
    entry = text_entry.get('1.0', 'end-1c').strip()  # Remove trailing newlines
    if not entry:
        messagebox.showwarning("Warning", "The diary entry is empty. Nothing was saved.")
        return

    file_path = os.path.join(directory_name, file_name + '.txt')
    try:
        with open(file_path, 'w') as file:
            file.write(entry)
        messagebox.showinfo("Success", f"Entry saved as {file_path}")
    except OSError as e:
        messagebox.showerror("Error", f"Failed to save entry: {e}")

# GUI Setup
root = tk.Tk()
root.title('Diary')

# Text Entry Box
text_entry = tk.Text(root, height=20, width=50, wrap='word')
text_entry.pack(padx=10, pady=10)

# Save Button
save_button = tk.Button(root, text='Save', command=save_entry)
save_button.pack(side='left', padx=10, pady=10)

# Quit Button
quit_button = tk.Button(root, text='Quit', command=root.quit)
quit_button.pack(side='right', padx=10, pady=10)

# Ensure the directory exists when the program starts
create_directory()

# Start the Tkinter event loop
root.mainloop()
