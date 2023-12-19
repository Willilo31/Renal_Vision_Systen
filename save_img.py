import cv2
from ultralytics import YOLO

def main():
    model = YOLO("Renal_Model_S5.pt")
    class_names = ["Blue_Clamp", "Pull_Ring_T", "Pull_Ring_II", "Pull_Ring_III", "Red_Clamp", "White_Clamp", "White_Paper_Band"]

    cap = cv2.VideoCapture(0)
    cv2.namedWindow("frame", cv2.WINDOW_NORMAL)

    while True:
        ret, frame = cap.read()

        if not ret:
            continue

        results = model.predict(frame, verbose=False, agnostic_nms=True, conf=0.50, imgsz=1280)


        if results is not None:
            for result in results:
                if result.boxes:
                    for box in result.boxes:
                        class_id = int(box.cls[0].item())
                        cords = box.xyxy[0].tolist()
                        x1, y1, x2, y2 = map(int, cords)

                        if class_id == 0: #Blue_Clamp
                                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4)
                                cv2.putText(frame, f"{class_names[class_id]}",(x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,)
                        
                        if class_id == 1: #Pull_Ring_T
                                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4)
                                cv2.putText(frame, f"{class_names[class_id]}",(x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,)

                        if class_id == 2: #Pull_Ring_II
                                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4)
                                cv2.putText(frame, f"{class_names[class_id]}",(x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,)                    

                        if class_id == 3: #Pull_Ring_III
                                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4)
                                cv2.putText(frame, f"{class_names[class_id]}",(x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,)

                        if class_id == 4: #Red_Clamp
                                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4)
                                cv2.putText(frame, f"{class_names[class_id]}",(x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,)

                        if class_id == 5: #White_Clamp
                                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4)
                                cv2.putText(frame, f"{class_names[class_id]}",(x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,)
                        
                        if class_id == 6: #White_Paper_Band
                                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4)
                                cv2.putText(frame, f"{class_names[class_id]}",(x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,)
                        
        cv2.imshow("frame", frame)
        if (cv2.waitKey(1) & 0xFF == ord('q')):
                cv2.destroyAllWindows()
                break

if __name__=="__main__":
    main()


Tengo este que funciona para captar algunos componentes de imagenes. 
Quisiera que al ver clase de los clamp, es decir clase 0, 4, 5. haga un Frame2 con la dimensiones que tiene en x1, y1, x2, y2, es decir:
frame2 = frame[y1:y2, x1:x2] y ese frame 2 lo guarde en una nueva carpeta, que la cree si no existe que se llama Frame_reducidos. 
Las detecciones en ves de hacerlo el tiempo real, que lo haga de imagenes, pero de imagenes de una carpeta que se llama IMGZ que tiene mas de 1000 imagenes llamadas 
Frame Frame_001.jpg, Frame_002.jpg, Frame_003.jpg y asi sucesivamente. 