import cv2
import time
from datetime import datetime

# Load the XML file you just fixed
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

detection = False
detection_stopped_time = None
timer_started = False
SECONDS_TO_RECORD_AFTER_DETECTION = 5

frame_size = (int(cap.get(3)), int(cap.get(4)))
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = None

print("Main Surveillance System Running... Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret: break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) > 0:
        if not detection:
            detection = True
            current_time = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            out = cv2.VideoWriter(f"video_{current_time}.mp4", fourcc, 20, frame_size)
            print("Movement detected! Recording...")
        timer_started = False
    elif detection:
        if not timer_started:
            timer_started = True
            detection_stopped_time = time.time()
        
        if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
            detection = False
            timer_started = False
            out.release()
            print('Recording stopped and saved.')

    if detection:
        out.write(frame)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("Main Feed", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()