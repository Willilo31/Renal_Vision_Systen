import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk 
import cv2
import imutils
import numpy as np
from datetime import datetime
from ultralytics import YOLO
import subprocess
import os 

Salida = 11
energy_cut = 13

def visualizar():
    global model, cap, frame, class_names

    if inicio == 1:
        model = YOLO("Renal_Model_S2.pt")
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
        class_names = ["Blue_Clamp", "Pull_Ring_T", "Pull_Ring_II", "Pull_Ring_III", "Red_Clamp", "White_Clamp", "White_Paper_Band"]
        inicio = 0

    else:
        pantalla.delete(frame)
    
    if cap is not None:
        ret, frame = cap.read()

        if ret == True:
            results = model.predict(frame, verbose=False, agnostic_nms=True, conf = 0.50, imgsz = 416, device = 0)
            height, width, _ = frame.shape

            if results is not None:
                for result in results:
                    if result.boxes:
                        for box in result.boxes:
                            class_id = int(box.cls[0].item())
                            cords = box.xyxy[0].tolist()
                            x1, y1, x2, y2 = map(int, cords)

                            if class_id == 0: 
                                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 255), 4)
                                cv2.putText(frame, f"{class_names[0]}", (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2,)
                        
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = imutils.resize(frame, width=1000, height=562)

            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)

            lblVideo.configure(image=img)
            lblVideo.image = img
            
            pantalla.after(10, visualizar)
        else:
            cap.release()

def turn_off_action():
    root.destroy()

root = tk.Tk()
root.title("Renal Vision System")

root.attributes('-fullscreen', True)

pantalla = tk.Canvas(root, width=1920, height=1080, bg="#FFFFFF")
pantalla.pack()

#Boton de cerrado
Close = tk.PhotoImage(file="IMG/shutdown.png")
Close_Button = tk.Button(pantalla, image=Close, bg="#FFFFFF", command=turn_off_action, borderwidth=0, relief="flat")
Close_Button.place(x = 1794, y = 55)

lblVideo = tk.Label(pantalla)
lblVideo.configure(borderwidth=0)
lblVideo.place(x = 180, y = 100)
inicio = 1

visualizar()

#FFFFFF -> Blanco
#FF0035 -> Rojo
#008000 -> verde

root.mainloop()
