import cv2
from ultralytics import YOLO

def main():
    model = YOLO("Renal_Model_S1.pt")
    class_names = ["Blue_Clamp", "Pull_Ring_T", "Pull_Ring_II", "Pull_Ring_III", "Red_Clamp", "White_Clamp", "White_Paper_Band"]    

    cap = cv2.VideoCapture(0)
    cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
    Counter_Blue_Clamp = 0
    Counter_Pull_Ring_T = 0
    Counter_Pull_Ring_II = 0
    Counter_Pull_Ring_III = 0
    Counter_Red_Clamp = 0
    Counter_White_Clamp = 0
    Counter_White_Paper_Band = 0
    while True:
        ret, frame = cap.read()

        if not ret:
            continue

        results = model.predict(frame, verbose=False, agnostic_nms=True, conf=0.50, imgsz=640)
        
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
                                Counter_Blue_Clamp+=1
                        
                        if class_id == 1: #Pull_Ring_T
                                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4)
                                cv2.putText(frame, f"{class_names[class_id]}",(x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,)
                                Counter_Pull_Ring_T+=1

                        if class_id == 2: #Pull_Ring_II
                                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4)
                                cv2.putText(frame, f"{class_names[class_id]}",(x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,)                    
                                Counter_Pull_Ring_II+=1

                        if class_id == 3: #Pull_Ring_III
                                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4)
                                cv2.putText(frame, f"{class_names[class_id]}",(x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,)
                                Counter_Pull_Ring_III+=1

                        if class_id == 4: #Red_Clamp
                                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4)
                                cv2.putText(frame, f"{class_names[class_id]}",(x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,)
                                Counter_Red_Clamp+=1

                        if class_id == 5: #White_Clamp
                                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4)
                                cv2.putText(frame, f"{class_names[class_id]}",(x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,)
                                Counter_White_Clamp+=1

                        if class_id == 6: #White_Paper_Band
                                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4)
                                cv2.putText(frame, f"{class_names[class_id]}",(x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,)
                                Counter_White_Paper_Band+=1
                else:
                    Counter_Blue_Clamp = 0
                    Counter_Pull_Ring_T = 0
                    Counter_Pull_Ring_II = 0
                    Counter_Pull_Ring_III = 0
                    Counter_Red_Clamp = 0
                    Counter_White_Clamp = 0
                    Counter_White_Paper_Band = 0

        print(f'Blue_Clamp:-------->{Counter_Blue_Clamp}/1')
        print(f'Pull_Ring_T:------->{Counter_Pull_Ring_T}/4')
        print(f'Pull_Ring_II:------>{Counter_Pull_Ring_II}/1')
        print(f'Pull_Ring_III:----->{Counter_Pull_Ring_III}/1')
        print(f'Red_Clamp:--------->{Counter_Red_Clamp}/1')
        print(f'White_Clamp:------->{Counter_White_Clamp}/3')
        print(f'White_Paper_Band:-->{Counter_White_Paper_Band}/2')

        Counter_Blue_Clamp = 0
        Counter_Pull_Ring_T = 0
        Counter_Pull_Ring_II = 0
        Counter_Pull_Ring_III = 0
        Counter_Red_Clamp = 0
        Counter_White_Clamp = 0
        Counter_White_Paper_Band = 0
        
        cv2.imshow("frame", frame)
        if (cv2.waitKey(1) == 27):
            cv2.destroyAllWindows()
            break

if __name__=="__main__":
    main()

# Blue_Clamp → 1
# Pull_Ring_T → 4 
# Pull_Ring_II → 1
# Pull_Ring_III → 1
# Red_Clamp → 1 
# White_Clamp → 3
# White_Paper_Band → 2


