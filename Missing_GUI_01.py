import tkinter as tk
from PIL import Image, ImageTk 
import cv2
import imutils
from ultralytics import YOLO
from statistics import mode
import Jetson.GPIO as GPIO

def visualizar():
    global inicio, model, cap, frame, class_names, cambio, button, camera_id
    global Counter_Blue_Clamp, Counter_Pull_Ring_T, Counter_Pull_Ring_II, Counter_Pull_Ring_III, Counter_Red_Clamp, Counter_White_Clamp, Counter_White_Paper_Band
    global Vector_Blue_Clamp, Vector_Pull_Ring_T, Vector_Pull_Ring_II, Vector_Pull_Ring_III, Vector_Red_Clamp, Vector_White_Clamp, Vector_White_Paper_Band
    global Text_Blue_Clamp, Text_Pull_Ring_T, Text_Pull_Ring_II, Text_Pull_Ring_III, Text_Red_Clamp, Text_White_Clamp, Text_White_Paper_Band

    if inicio == 1:
        inicio = 0
        button = 13
        model = YOLO("Models/Missing_Component_S5.pt")

        class_names = ["Blue_Clamp", "Pull_Ring_T", "Pull_Ring_II", "Pull_Ring_III", "Red_Clamp", "White_Clamp", "White_Paper_Band"]
        cap = cv2.VideoCapture(2)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)        
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(button, GPIO.IN)

        #Variables
        Counter_Blue_Clamp = 0
        Counter_Pull_Ring_T = 0
        Counter_Pull_Ring_II = 0
        Counter_Pull_Ring_III = 0
        Counter_Red_Clamp = 0
        Counter_White_Clamp = 0
        Counter_White_Paper_Band = 0
        camera_id = 0
        
        #Vector
        Vector_Blue_Clamp = []
        Vector_Pull_Ring_T = []
        Vector_Pull_Ring_II = []
        Vector_Pull_Ring_III = []
        Vector_Red_Clamp = []
        Vector_White_Clamp = []
        Vector_White_Paper_Band = []
        cambio = True
    
    else:
        pantalla.delete(frame)
    
    if cap is not None:
        ret, frame = cap.read()

        if ret == True:
            results = model.predict(frame, verbose=True, agnostic_nms=True, conf = 0.50, imgsz = 1280, half = True, device = 0)
            
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
                                    
                                    x1 = 0
                                    x2 = 0
                                    y1 = 0
                                    y2 = 0
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
                    
                    if len(Vector_Blue_Clamp) >= 5:
                        cambio = True #Cambio debe de ser falso

                        pantalla.delete(Text_Blue_Clamp, Text_Pull_Ring_T, Text_Pull_Ring_II, Text_Pull_Ring_III, Text_Red_Clamp, Text_White_Clamp, Text_White_Paper_Band)
                        
                        if mode(Vector_Blue_Clamp) == 1: Text_Blue_Clamp = pantalla.create_text(1248, 300, text=f"{mode(Vector_Blue_Clamp)}/1 ➞ Blue Clamp", font=("Helvetica", 30, "bold"), fill="black", anchor=tk.NW)
                        else: Text_Blue_Clamp = pantalla.create_text(1248, 300, text=f"{mode(Vector_Blue_Clamp)}/1 ➞ Blue Clamp", font=("Helvetica", 30, "bold"), fill="red", anchor=tk.NW)

                        if mode(Vector_Pull_Ring_T) == 4: Text_Pull_Ring_T = pantalla.create_text(1248, 371, text=f"{mode(Vector_Pull_Ring_T)}/4 ➞ Pull Ring T", font=("Helvetica", 30, "bold"), fill="black", anchor=tk.NW)
                        else: Text_Pull_Ring_T = pantalla.create_text(1248, 371, text=f"{mode(Vector_Pull_Ring_T)}/4 ➞ Pull Ring T", font=("Helvetica", 30, "bold"), fill="red", anchor=tk.NW)

                        if mode(Vector_Pull_Ring_II) == 1: Text_Pull_Ring_II = pantalla.create_text(1248, 443, text=f"{mode(Vector_Pull_Ring_II)}/1 ➞ Pull Ring II", font=("Helvetica", 30, "bold"), fill="black", anchor=tk.NW)
                        else: Text_Pull_Ring_II = pantalla.create_text(1248, 443, text=f"{mode(Vector_Pull_Ring_II)}/1 ➞ Pull Ring II", font=("Helvetica", 30, "bold"), fill="red", anchor=tk.NW)

                        if mode(Vector_Pull_Ring_III) == 1: Text_Pull_Ring_III = pantalla.create_text(1248, 515, text=f"{mode(Vector_Pull_Ring_III)}/1 ➞ Pull Ring III", font=("Helvetica", 30, "bold"), fill="black", anchor=tk.NW)
                        else: Text_Pull_Ring_III = pantalla.create_text(1248, 515, text=f"{mode(Vector_Pull_Ring_III)}/1 ➞ Pull Ring III", font=("Helvetica", 30, "bold"), fill="red", anchor=tk.NW)
                        
                        if mode(Vector_Red_Clamp) == 1: Text_Red_Clamp = pantalla.create_text(1248, 589, text=f"{mode(Vector_Red_Clamp)}/1 ➞ Red Clamp", font=("Helvetica", 30, "bold"), fill="black", anchor=tk.NW)
                        else: Text_Red_Clamp = pantalla.create_text(1248, 589, text=f"{mode(Vector_Red_Clamp)}/1 ➞ Red Clamp", font=("Helvetica", 30, "bold"), fill="red", anchor=tk.NW)

                        if mode(Vector_White_Clamp) == 3: Text_White_Clamp = pantalla.create_text(1248, 661, text=f"{mode(Vector_White_Clamp)}/3 ➞ White Clamp", font=("Helvetica", 30, "bold"), fill="black", anchor=tk.NW)
                        else: Text_White_Clamp = pantalla.create_text(1248, 661, text=f"{mode(Vector_White_Clamp)}/3 ➞ White Clamp", font=("Helvetica", 30, "bold"), fill="red", anchor=tk.NW)
                        
                        if mode(Vector_White_Paper_Band) == 2: Text_White_Paper_Band  = pantalla.create_text(1248, 733, text=f"{mode(Vector_White_Paper_Band)}/2 ➞ White Paper Band", font=("Helvetica", 30, "bold"), fill="black", anchor=tk.NW)
                        else: Text_White_Paper_Band  = pantalla.create_text(1248, 733, text=f"{mode(Vector_White_Paper_Band)}/2 ➞ White Paper Band", font=("Helvetica", 30, "bold"), fill="red", anchor=tk.NW)
                        
                        Vector_Blue_Clamp = []
                        Vector_Pull_Ring_T = []
                        Vector_Pull_Ring_II = []
                        Vector_Pull_Ring_III = []
                        Vector_Red_Clamp = []
                        Vector_White_Clamp = []
                        Vector_White_Paper_Band = []
            else:
                cambio = True
            
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = imutils.resize(frame, width=1000, height=562)

            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)

            lblVideo.configure(image=img)
            lblVideo.image = img
            
            pantalla.after(10, visualizar)
        else:
            cap = cv2.VideoCapture(camera_id)
            cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
            print("La camara id es: ",camera_id)
            camera_id +=1
            if camera_id >= 10:
                camera_id = 0
            pantalla.after(100, visualizar)

def turn_off_action():
    root.destroy()

root = tk.Tk()
root.title("Renal Vision System")

# root.geometry("1000x700")
root.attributes('-fullscreen', True)

pantalla = tk.Canvas(root, width=1920, height=1080, bg="#FFFFFF")
pantalla.pack()

Titulo = pantalla.create_text(157, 110, text="Renal Vision System", font=("Helvetica", 40, "bold"), fill="black", anchor=tk.NW)

#Boton de cerrado
Close = tk.PhotoImage(file="IMG/shutdown.png")
Close_Button = tk.Button(pantalla, image=Close, bg="#FFFFFF", command=turn_off_action, borderwidth=0, relief="flat")
Close_Button.place(x = 1794, y = 55)

lblVideo = tk.Label(pantalla)
lblVideo.configure(borderwidth=0)
lblVideo.place(x = 157, y = 259)
inicio = 1

Text_Blue_Clamp = pantalla.create_text(1248, 300, text=f"0/1 ➞ Blue Clamp", font=("Helvetica", 30, "bold"), fill="black", anchor=tk.NW)
Text_Pull_Ring_T = pantalla.create_text(1248, 371, text=f"0/4 ➞ Pull Ring T", font=("Helvetica", 30, "bold"), fill="black", anchor=tk.NW)
Text_Pull_Ring_II = pantalla.create_text(1248, 443, text=f"0/1 ➞ Pull Ring II", font=("Helvetica", 30, "bold"), fill="black", anchor=tk.NW)
Text_Pull_Ring_III = pantalla.create_text(1248, 515, text=f"0/1 ➞ Pull Ring III", font=("Helvetica", 30, "bold"), fill="black", anchor=tk.NW)
Text_Red_Clamp = pantalla.create_text(1248, 589, text=f"0/1 ➞ Red Clamp", font=("Helvetica", 30, "bold"), fill="black", anchor=tk.NW)
Text_White_Clamp = pantalla.create_text(1248, 661, text=f"0/3 ➞ White Clamp", font=("Helvetica", 30, "bold"), fill="black", anchor=tk.NW)
Text_White_Paper_Band  = pantalla.create_text(1248, 733, text=f"0/2 ➞ White Paper Band", font=("Helvetica", 30, "bold"), fill="black", anchor=tk.NW)

visualizar()

#FFFFFF -> Blanco
#FF0035 -> Rojo
#008000 -> verde

root.mainloop()
