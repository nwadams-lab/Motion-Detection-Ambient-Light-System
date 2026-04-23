import cv2
import serial
from ultralytics import YOLO
import time

# Connect to Arduino
ser = serial.Serial('COM9', 9600)

# Load YOLO model (pretrained)
model = YOLO("yolov8n.pt")  # lightweight + fast

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO detection
    results = model(frame, stream=True)

    human_detected = False

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])

            # Class 0 = person in YOLO
            if cls == 0:
                human_detected = True

                # Draw box
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
                cv2.putText(frame, "Human", (x1, y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

    if human_detected:
        print("Human detected!")
        ser.write(b'1')
        time.sleep(0.5)  
    else:
        print("No human detected.")
        ser.write(b'0')
        time.sleep(0.5)

    cv2.imshow("YOLO Detection", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()