import cv2
import numpy as np
from ultralytics import YOLO
import time

model = YOLO('Models/Missing_Component_S5.pt')

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Número de imágenes en cada lote (batch)
num_frames = 10
frames = []

# Inicializar el tiempo
prev_frame_time = time.time()
new_frame_time = 0

while cap.isOpened():
    success, frame = cap.read()

    if success:
        new_frame_time = time.time()

        frames.append(frame)

        if len(frames) == num_frames:
            # Realizar la inferencia en el lote de frames
            results = model(source=frames, device=0, imgsz=640, conf=0.50, agnostic_nms=True)

            # Iterar sobre los resultados del lote
            for i, result in enumerate(results):
                annotated_frame = result.plot()

                # Asegurarse de que el denominador no sea cero antes de calcular el FPS
                if new_frame_time != prev_frame_time:
                    fps = 1 / (new_frame_time - prev_frame_time)
                else:
                    fps = 0

                prev_frame_time = new_frame_time

                # Convierte el FPS a string para mostrarlo
                fps_text = f"FPS: {fps:.2f}"

                # Pone el FPS en el frame
                cv2.putText(annotated_frame, fps_text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

                # Muestra el frame
                cv2.imshow(f"Frame {i+1}", annotated_frame)

            frames = []  # Reiniciar la lista de frames

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()