import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import webbrowser

# Paths
attendance_file = "attendance.csv"

def register_face():
    name = entry_name.get().strip()
    if not name:
        messagebox.showwarning("Input Error", "Please enter a name!")
        return

    subprocess.run(["python", "register_face.py"], input=name.encode())

def start_attendance():
    subprocess.Popen(["python", "recognize_attendance.py"])

def open_attendance_file():
    if os.path.exists(attendance_file):
        webbrowser.open(attendance_file)
    else:
        messagebox.showinfo("Info", "No attendance file found yet.")

# GUI setup
app = tk.Tk()
app.title("Face Recognition Attendance System")
app.geometry("400x300")
app.resizable(False, False)

tk.Label(app, text="Enter Name to Register:", font=("Arial", 12)).pack(pady=10)
entry_name = tk.Entry(app, font=("Arial", 12))
entry_name.pack(pady=5)

tk.Button(app, text="Register Face", font=("Arial", 12), command=register_face).pack(pady=10)
tk.Button(app, text="Start Attendance", font=("Arial", 12), command=start_attendance).pack(pady=10)
tk.Button(app, text="Open Attendance File", font=("Arial", 12), command=open_attendance_file).pack(pady=10)

tk.Label(app, text="Press 'q' to exit live camera", font=("Arial", 10, "italic")).pack(pady=20)

app.mainloop()
