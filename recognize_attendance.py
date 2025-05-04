import cv2
import face_recognition
import pickle
import numpy as np
import csv
from datetime import datetime
import os

encodings_path = "encodings/encodings.pkl"
attendance_file = "attendance.csv"

# Load known face encodings
if not os.path.exists(encodings_path):
    print("[ERROR] No encodings found! Please register faces first.")
    exit()

with open(encodings_path, "rb") as f:
    known_encodings = pickle.load(f)

known_face_encodings = list(known_encodings.values())
known_face_names = list(known_encodings.keys())

# Initialize webcam
video_capture = cv2.VideoCapture(0)
print("[INFO] Starting face recognition. Press 'q' to quit.")

# Marked attendance tracker
attendance_marked = set()

def mark_attendance(name):
    now = datetime.now()
    dt_string = now.strftime('%Y-%m-%d %H:%M:%S')

    if not os.path.exists(attendance_file):
        with open(attendance_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Name', 'DateTime'])

    with open(attendance_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, dt_string])
        print(f"[INFO] Marked attendance for {name} at {dt_string}")

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("[ERROR] Failed to capture video.")
        break

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        top, right, bottom, left = [v * 4 for v in face_location]
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left + 5, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

        # Mark attendance once per session
        if name != "Unknown" and name not in attendance_marked:
            mark_attendance(name)
            attendance_marked.add(name)

    cv2.imshow('Face Recognition Attendance', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
