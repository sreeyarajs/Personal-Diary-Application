# Personal-Diary-Application

#### Description:
This Python application allows users to write and save their daily diary entries using a simple graphical interface created with Tkinter. Each diary entry is saved in a date-specific directory, with the filename including the current date and time. The app ensures that the directory for the current date exists and provides messages to notify users of successful saves or any errors.

#### Code Explanation:
1. **Imports**:
   - `datetime`: Used to get the current date and time for naming files and directories.
   - `os`: Handles directory and file operations, such as creating directories and saving files.
   - `tkinter`: Creates the graphical user interface for the diary application, including buttons and text entry areas.
   - `messagebox`: Provides popup dialogs to show success or error messages.

2. **Functions**:
   - `create_directory()`: Creates a directory for the current date (if it doesn't already exist) to store daily entries.
   - `save_entry()`: Saves the user's diary entry into a text file, naming the file based on the current date and time. The content is saved inside the corresponding date directory.

3. **GUI Setup**:
   - `tkinter.Text`: A text box for entering diary entries.
   - `tkinter.Button`: Buttons for saving the entry and quitting the application.
   - `messagebox.showinfo()`, `messagebox.showwarning()`, and `messagebox.showerror()`: Used to show success, warning, or error messages to the user.

4. **Directory Creation**:
   - When the program starts, it ensures that the directory for today's date is created. The `save_entry()` function uses this directory to store entries.

---

### Features:
- **Directory Creation**: Each day's diary entries are saved in a folder named with the current date (e.g., `2024-11-22`).
- **Automatic File Naming**: Diary entries are saved with filenames including the current date and time (e.g., `2024-11-22_14-30-45.txt`).
- **Warning for Empty Entries**: If the user attempts to save an empty entry, a warning message is shown.
- **Error Handling**: If there is an issue with creating a directory or saving the file, appropriate error messages are displayed.

---

### Usage:

1. **Clone the Repository**:
   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/personal-diary.git
   cd personal-diary
   ```

2. **Run the Application**:
   Ensure you have Python installed (preferably Python 3.x) and that Tkinter is available. Run the application:

   ```bash
   python diary_app.py
   ```

3. **Using the Diary**:
   - Open the application, and you will see a text box where you can write your diary entry.
   - Click the **Save** button to save the entry for the current day. The file will be saved in a folder named after the current date, with a timestamped filename.
   - Click **Quit** to close the application.

---

### Screenshot:

1. **Main Interface**:
   <img width="314" alt="{905516AF-20DB-424F-872C-08022A94C25E}" src="https://github.com/user-attachments/assets/09f1261e-a621-4af5-9280-6585c5afdd2f">
   <img width="315" alt="{4A4A224F-C64C-4A1A-BA14-FD0F6C1EF37E}" src="https://github.com/user-attachments/assets/dc043c62-2ee3-4ba9-99b3-b7f87f35145b">



2. **Saved Entry Notification**:
   <img width="313" alt="{F6E5ED94-D60F-407D-934D-389192F5D657}" src="https://github.com/user-attachments/assets/24f2edc3-7cb9-48c0-8054-30b9a115ff62">
