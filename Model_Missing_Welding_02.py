import cv2
from ultralytics import YOLO
import Jetson.GPIO as GPIO
from statistics import mode

def main():
        button = 13
        model_Missing= YOLO("Models/Missing_Component_S5.pt")
        model_Insertion= YOLO("Models/Welding_Insertion_S02.pt")

        class_names_Missing = ["Blue_Clamp", "Pull_Ring_T", "Pull_Ring_II", "Pull_Ring_III", "Red_Clamp", "White_Clamp", "White_Paper_Band"]
        class_names_Insertion = ["Complete", "Good", "Incomplete"]

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(button, GPIO.IN)

        cap_Missing = cv2.VideoCapture(2)
        cap_Missing.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
        cap_Missing.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
        cv2.namedWindow("Missing Components", cv2.WINDOW_NORMAL)

        cap_Insertion = cv2.VideoCapture(0)
        cap_Insertion.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
        cap_Insertion.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
        cv2.namedWindow("Welding and Insertion", cv2.WINDOW_NORMAL)

        #Variables Missing Components
        Counter_Blue_Clamp = 0
        Counter_Pull_Ring_T = 0
        Counter_Pull_Ring_II = 0
        Counter_Pull_Ring_III = 0
        Counter_Red_Clamp = 0
        Counter_White_Clamp = 0
        Counter_White_Paper_Band = 0

        #Variables Welding and Insertion
        Counter_Complete_Insertion = 0
        Counter_Good_Weld = 0
        Counter_Incomplete_Insertion = 0

        #Vector Missing Components 
        Vector_Blue_Clamp = []
        Vector_Pull_Ring_T = []
        Vector_Pull_Ring_II = []
        Vector_Pull_Ring_III = []
        Vector_Red_Clamp = []
        Vector_White_Clamp = []
        Vector_White_Paper_Band = []

        #Vector Missing Components 
        Vector_Complete_Insertion  = []
        Vector_Good_Weld = []
        Vector_Incomplete_Insertion = []

        cambio = True

        while True:
                ret_Missing, frame_Missing = cap_Missing.read()

                ret_Insertion, frame_Insertion = cap_Insertion.read()

                if not ret_Missing:
                        continue

                if not ret_Insertion:
                        continue

                results_Missing = model_Missing.predict(frame_Missing, verbose=True, agnostic_nms=True, conf=0.50, imgsz=640)

                results_Insertion = model_Insertion.predict(frame_Insertion, verbose=True, agnostic_nms=True, conf=0.25, imgsz=1280)

                if not GPIO.input(button):
                        if cambio == True:
                                if results_Missing is not None:
                                        for result_Missing in results_Missing:
                                                if result_Missing.boxes:
                                                        for box in result_Missing.boxes:
                                                                class_id = int(box.cls[0].item())
                                                                cords = box.xyxy[0].tolist()
                                                                x1, y1, x2, y2 = map(int, cords)

                                                                if class_id == 0: #Blue_Clamp
                                                                        cv2.rectangle(frame_Missing, (x1, y1), (x2, y2), (0, 255, 0), 4)
                                                                        cv2.putText(frame_Missing, f"{class_names_Missing[class_id]}",(x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,)
                                                                        Counter_Blue_Clamp+=1
                                                                
                                                                if class_id == 1: #Pull_Ring_T
                                                                        cv2.rectangle(frame_Missing, (x1, y1), (x2, y2), (0, 255, 0), 4)
                                                                        cv2.putText(frame_Missing, f"{class_names_Missing[class_id]}",(x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,)
                                                                        Counter_Pull_Ring_T+=1

                                                                if class_id == 2: #Pull_Ring_II
                                                                        cv2.rectangle(frame_Missing, (x1, y1), (x2, y2), (0, 255, 0), 4)
                                                                        cv2.putText(frame_Missing, f"{class_names_Missing[class_id]}",(x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,)                    
                                                                        Counter_Pull_Ring_II+=1

                                                                if class_id == 3: #Pull_Ring_III
                                                                        cv2.rectangle(frame_Missing, (x1, y1), (x2, y2), (0, 255, 0), 4)
                                                                        cv2.putText(frame_Missing, f"{class_names_Missing[class_id]}",(x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,)
                                                                        Counter_Pull_Ring_III+=1

                                                                if class_id == 4: #Red_Clamp
                                                                        cv2.rectangle(frame_Missing, (x1, y1), (x2, y2), (0, 255, 0), 4)
                                                                        cv2.putText(frame_Missing, f"{class_names_Missing[class_id]}",(x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,)
                                                                        Counter_Red_Clamp+=1

                                                                if class_id == 5: #White_Clamp
                                                                        cv2.rectangle(frame_Missing, (x1, y1), (x2, y2), (0, 255, 0), 4)
                                                                        cv2.putText(frame_Missing, f"{class_names_Missing[class_id]}",(x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,)
                                                                        Counter_White_Clamp+=1

                                                                if class_id == 6: #White_Paper_Band
                                                                        cv2.rectangle(frame_Missing, (x1, y1), (x2, y2), (0, 255, 0), 4)
                                                                        cv2.putText(frame_Missing, f"{class_names_Missing[class_id]}",(x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,)
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
                                
                                if results_Insertion is not None:
                                        for result_Insertion in results_Insertion:
                                                if result_Insertion.boxes:
                                                        for box in result_Insertion.boxes:
                                                                class_id = int(box.cls[0].item())
                                                                cords = box.xyxy[0].tolist()
                                                                x1, y1, x2, y2 = map(int, cords)

                                                                if class_id == 0: #Complete Insertion
                                                                        cv2.rectangle(frame_Insertion, (x1, y1), (x2, y2), (0, 255, 0), 4)
                                                                        cv2.putText(frame_Insertion, f"{class_names_Insertion[class_id]}",(x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,)
                                                                        Counter_Complete_Insertion+=1
                                                                
                                                                if class_id == 1: #Good Weld
                                                                        cv2.rectangle(frame_Insertion, (x1, y1), (x2, y2), (0, 255, 0), 4)
                                                                        cv2.putText(frame_Insertion, f"{class_names_Insertion[class_id]}",(x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,)
                                                                        Counter_Good_Weld+=1

                                                                if class_id == 2: #Incomplete Insertion
                                                                        cv2.rectangle(frame_Insertion, (x1, y1), (x2, y2), (0, 0, 255), 4)
                                                                        cv2.putText(frame_Insertion, f"{class_names_Insertion[class_id]}",(x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2,)                    
                                                                        Counter_Incomplete_Insertion+=1
                                                else:
                                                        Counter_Complete_Insertion = 0
                                                        Counter_Good_Weld = 0
                                                        Counter_Incomplete_Insertion = 0
                                
                                Vector_Complete_Insertion.append(Counter_Complete_Insertion)
                                Vector_Good_Weld.append(Counter_Good_Weld)
                                Vector_Incomplete_Insertion.append(Counter_Incomplete_Insertion)

                                Counter_Complete_Insertion = 0
                                Counter_Good_Weld = 0
                                Counter_Incomplete_Insertion = 0

                                if len(Vector_Blue_Clamp) >= 10:
                                        # cambio = False
                                        print(f' ') 
                                        print(f'======================')                                   
                                        print(f'  Missing Components  ')                                   
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

                                        print(f' ')                                   
                                        print(f'======================')                                   
                                        print(f'Welding and Insertion ')                                   
                                        print(f'======================')                                   
                                        print(f'Complete Insertion:-------->{mode(Vector_Complete_Insertion)}')
                                        print(f'Good Weld:------->{mode(Vector_Good_Weld)}')
                                        print(f'Incomplete Insertion:------>{mode(Vector_Incomplete_Insertion)}')
                                        print(f'======================')
                                        
                                        Vector_Complete_Insertion = []
                                        Vector_Good_Weld = []
                                        Vector_Incomplete_Insertion = []
                
                else:
                        cambio = True
                cv2.imshow("Missing Components", frame_Missing)
                cv2.imshow("Welding and Insertion", frame_Insertion)
                
                if (cv2.waitKey(1) & 0xFF == ord('q')):
                        cv2.destroyAllWindows()
                        break
        
if __name__=="__main__":
        main()
