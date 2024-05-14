import cv2
from ultralytics import YOLO
import time

model = YOLO('Models/Tube_Position_N02.pt')

cap = cv2.VideoCapture(4)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)

while cap.isOpened():
    success, frame = cap.read()

    if success:
        new_frame_time = time.time()

        results = model(frame, device=0, imgsz=640, conf=0.60, agnostic_nms=True)
        annotated_frame = results[0].plot()
        cv2.imshow("Frame", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
