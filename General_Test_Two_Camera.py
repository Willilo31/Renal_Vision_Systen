import cv2
from ultralytics import YOLO
import time

model = YOLO('Models/Missing_Component_S5.pt')
model2 = YOLO('Models/Welding_Insertion_S02.pt')

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

cap2 = cv2.VideoCapture(2)
cap2.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Inicializar el tiempo
prev_frame_time = time.time()
new_frame_time = 0

while cap.isOpened():
    success, frame = cap.read()
    success2, frame2 = cap2.read()

    if success:
        new_frame_time = time.time()

        results = model(frame, device=0, imgsz=1280, conf=0.50, agnostic_nms=True)
        results2 = model2(frame2, device=0, imgsz=640, conf=0.50, agnostic_nms=True)

        annotated_frame = results[0].plot()
        annotated_frame2 = results2[0].plot()

        # Calcula FPS
        fps = 1/(new_frame_time-prev_frame_time)
        prev_frame_time = new_frame_time

        # Convierte el FPS a string para mostrarlo
        fps_text = f"FPS: {fps:.2f}"

        # Pone el FPS en el frame
        cv2.putText(annotated_frame, fps_text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(annotated_frame2, fps_text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow("Frame", annotated_frame)
        cv2.imshow("Frame2", annotated_frame2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
