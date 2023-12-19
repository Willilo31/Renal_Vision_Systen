import cv2
from ultralytics import YOLO


model = YOLO('Renal_Model_S5.pt')
cap = cv2.VideoCapture(6)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,740)

while cap.isOpened():

    success, frame = cap.read()

    if success:
        results = model(frame, device=0, imgsz=1280, conf=0.25, agnostic_nms=True)

        annotated_frame = results[0].plot()

        cv2.imshow("YOLOv8 Inference", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
