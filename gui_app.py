# import tkinter as tk
# from tkinter import messagebox
# import subprocess
# import os
# import webbrowser

# # Paths
# attendance_file = "attendance.csv"

# def register_face():
#     name = entry_name.get().strip()
#     if not name:
#         messagebox.showwarning("Input Error", "Please enter a name!")
#         return

#     subprocess.run(["python", "register_face.py"], input=name.encode())

# def start_attendance():
#     subprocess.Popen(["python", "recognize_attendance.py"])

# def open_attendance_file():
#     if os.path.exists(attendance_file):
#         webbrowser.open(attendance_file)
#     else:
#         messagebox.showinfo("Info", "No attendance file found yet.")

# # GUI setup
# app = tk.Tk()
# app.title("Face Recognition Attendance System")
# app.geometry("400x300")
# app.resizable(False, False)

# tk.Label(app, text="Enter Name to Register:", font=("Arial", 12)).pack(pady=10)
# entry_name = tk.Entry(app, font=("Arial", 12))
# entry_name.pack(pady=5)

# tk.Button(app, text="Register Face", font=("Arial", 12), command=register_face).pack(pady=10)
# tk.Button(app, text="Start Attendance", font=("Arial", 12), command=start_attendance).pack(pady=10)
# tk.Button(app, text="Open Attendance File", font=("Arial", 12), command=open_attendance_file).pack(pady=10)

# tk.Label(app, text="Press 'q' to exit live camera", font=("Arial", 10, "italic")).pack(pady=20)

# app.mainloop()
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
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

# Setup root window
app = tk.Tk()
app.title("✨ Face Recognition Attendance System ✨")
app.geometry("800x500")
app.resizable(False, False)

# Background image
bg_image = Image.open("background.jpg")
bg_image = bg_image.resize((800, 500), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(app, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Overlay container
overlay = tk.Frame(app, bg="#000000", bd=0)
overlay.place(relx=0.5, rely=0.5, anchor='center')

# Title
title_label = tk.Label(app, text="Face Attendance System", font=("Helvetica", 28, "bold"),
                       bg="#003366", fg="#ffffff")
title_label.place(relx=0.5, rely=0.1, anchor="center")

# Entry box
entry_name = tk.Entry(app, font=("Helvetica", 16), bg="#f0f0f0", fg="#333", justify="center",
                      width=30, bd=2, relief="ridge")
entry_name.place(relx=0.5, rely=0.3, anchor="center")

# Animated Button Hover Effect
def on_enter(e):
    e.widget['background'] = "#0f9d58"
    e.widget['foreground'] = "#fff"

def on_leave(e):
    e.widget['background'] = "#34a853"
    e.widget['foreground'] = "#fff"

# Styled Buttons
def create_button(text, command, y):
    btn = tk.Button(app, text=text, font=("Helvetica", 14, "bold"), bg="#34a853", fg="white",
                    activebackground="#0f9d58", padx=20, pady=10, command=command, bd=0,
                    cursor="hand2", relief="flat")
    btn.place(relx=0.5, rely=y, anchor="center")
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    return btn

btn_register = create_button("Register Face", register_face, 0.45)
btn_attendance = create_button("Start Attendance", start_attendance, 0.57)
btn_open_csv = create_button("Open Attendance File", open_attendance_file, 0.69)

# Footer
footer = tk.Label(app, text="© 2025 FaceTrack | Powered by Python", font=("Arial", 10, "italic"),
                  bg="#000000", fg="#999999")
footer.place(relx=0.5, rely=0.95, anchor="center")

app.mainloop()
