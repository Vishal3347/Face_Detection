import cv2
import time
from datetime import datetime

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video = cv2.VideoCapture(0)

last_saved_time = 0 
COOLDOWN_SECONDS = 5 # It will wait 5 seconds before taking another photo

print("Photo Capture System Running... Press 'q' to quit.")

while True:
    check, frame = video.read()
    if frame is not None:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 10)

        current_time = time.time()

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            
            # Check if 5 seconds have passed since the last photo
            if current_time - last_saved_time > COOLDOWN_SECONDS:
                exact_time = datetime.now().strftime('%H-%M-%S')
                filename = f"face_detected_{exact_time}.jpg"
                cv2.imwrite(filename, frame)
                print(f"Photo Saved: {filename}")
                last_saved_time = current_time

        cv2.imshow("Photo Capture Feed", frame)
        if cv2.waitKey(1) == ord('q'):
            break

video.release()
cv2.destroyAllWindows()