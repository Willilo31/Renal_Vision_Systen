import cv2
from ultralytics import YOLO
import Jetson.GPIO as GPIO
from statistics import mode

def main():
        button = 13
        model = YOLO("Renal_Model_S2.pt")
        class_names = ["Blue_Clamp", "Pull_Ring_T", "Pull_Ring_II", "Pull_Ring_III", "Red_Clamp", "White_Clamp", "White_Paper_Band"]
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(button, GPIO.IN)

        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
        cv2.namedWindow("frame", cv2.WINDOW_NORMAL)

        #Variables
        Counter_Blue_Clamp = 0
        Counter_Pull_Ring_T = 0
        Counter_Pull_Ring_II = 0
        Counter_Pull_Ring_III = 0
        Counter_Red_Clamp = 0
        Counter_White_Clamp = 0
        Counter_White_Paper_Band = 0

        #Vector
        Vector_Blue_Clamp = []
        Vector_Pull_Ring_T = []
        Vector_Pull_Ring_II = []
        Vector_Pull_Ring_III = []
        Vector_Red_Clamp = []
        Vector_White_Clamp = []
        Vector_White_Paper_Band = []

        cambio = True

        while True:
                ret, frame = cap.read()

                if not ret:
                        continue

                results = model.predict(frame, verbose=False, agnostic_nms=True, conf=0.25, imgsz=1280)
                if not GPIO.input(button):
                        if cambio == True:
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
                                
                                Vector_Blue_Clamp.append(Counter_Blue_Clamp)
                                Vector_Pull_Ring_T.append(Counter_Pull_Ring_T)
                                Vector_Pull_Ring_II.append(Counter_Pull_Ring_II)
                                Vector_Pull_Ring_III.append(Counter_Pull_Ring_III)
                                Vector_Red_Clamp.append(Counter_Red_Clamp)
                                Vector_White_Clamp.append(Counter_White_Clamp)
                                Vector_White_Paper_Band.append(Counter_White_Paper_Band)

                                Counter_Blue_Clamp = 0
                                Counter_Pull_Ring_T = 0
                                Counter_Pull_Ring_II = 0
                                Counter_Pull_Ring_III = 0
                                Counter_Red_Clamp = 0
                                Counter_White_Clamp = 0
                                Counter_White_Paper_Band = 0
                                
                                if len(Vector_Blue_Clamp) >= 10:
                                        cambio = False
                                        print(f'======================')                                   
                                        print(f'Blue_Clamp:-------->{mode(Vector_Blue_Clamp)}/1')
                                        print(f'Pull_Ring_T:------->{mode(Vector_Pull_Ring_T)}/4')
                                        print(f'Pull_Ring_II:------>{mode(Vector_Pull_Ring_II)}/1')
                                        print(f'Pull_Ring_III:----->{mode(Vector_Pull_Ring_III)}/1')
                                        print(f'Red_Clamp:--------->{mode(Vector_Red_Clamp)}/1')
                                        print(f'White_Clamp:------->{mode(Vector_White_Clamp)}/3')
                                        print(f'White_Paper_Band:-->{mode(Vector_White_Paper_Band)}/2')
                                        print(f'======================')                      
                                        Vector_Blue_Clamp = []
                                        Vector_Pull_Ring_T = []
                                        Vector_Pull_Ring_II = []
                                        Vector_Pull_Ring_III = []
                                        Vector_Red_Clamp = []
                                        Vector_White_Clamp = []
                                        Vector_White_Paper_Band = []             
                else:
                        cambio = True
                cv2.imshow("frame", frame)
                if (cv2.waitKey(1) & 0xFF == ord('q')):
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


