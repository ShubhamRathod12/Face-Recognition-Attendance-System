import cv2
import face_recognition
import os
import pickle

# Paths
dataset_path = "dataset"
encodings_path = "encodings/encodings.pkl"

# Create folders if they don't exist
os.makedirs(dataset_path, exist_ok=True)
os.makedirs("encodings", exist_ok=True)

def register_face(name):
    cam = cv2.VideoCapture(0)
    print("[INFO] Starting camera. Look at the camera...")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("[ERROR] Failed to grab frame.")
            break

        cv2.imshow("Register - Press 's' to save", frame)
        key = cv2.waitKey(1)

        if key % 256 == ord('s'):
            image_path = os.path.join(dataset_path, f"{name}.jpg")
            cv2.imwrite(image_path, frame)
            print(f"[INFO] Saved image as {image_path}")
            break

    cam.release()
    cv2.destroyAllWindows()

    # Load the image and encode the face
    image = face_recognition.load_image_file(image_path)
    face_encodings = face_recognition.face_encodings(image)

    if not face_encodings:
        print("[ERROR] No face detected in the image!")
        os.remove(image_path)
        return

    encoding = face_encodings[0]

    # Save encoding
    if os.path.exists(encodings_path):
        with open(encodings_path, "rb") as f:
            all_encodings = pickle.load(f)
    else:
        all_encodings = {}

    all_encodings[name] = encoding

    with open(encodings_path, "wb") as f:
        pickle.dump(all_encodings, f)

    print(f"[INFO] Face for '{name}' registered successfully!")

if __name__ == "__main__":
    username = input("Enter name to register: ")
    register_face(username)
