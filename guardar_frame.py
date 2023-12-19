import os
import cv2
from ultralytics import YOLO

def main():
    model = YOLO("Renal_Model_S5.pt")
    class_names = ["Blue_Clamp", "Pull_Ring_T", "Pull_Ring_II", "Pull_Ring_III", "Red_Clamp", "White_Clamp", "White_Paper_Band"]

    # Crear directorio para guardar los recortes si no existe
    output_dir = "Frame_reducidos"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Carpeta con las imágenes
    img_folder = "IMGS"

    for img_file in os.listdir(img_folder):
        if img_file.endswith(".jpg"):
            img_path = os.path.join(img_folder, img_file)
            frame = cv2.imread(img_path)

            results = model.predict(frame, verbose=False, agnostic_nms=True, conf=0.50, imgsz=1280)

            if results is not None:
                for result in results:
                    if result.boxes:
                        for box in result.boxes:
                            class_id = int(box.cls[0].item())
                            cords = box.xyxy[0].tolist()
                            x1, y1, x2, y2 = map(int, cords)

                            if class_id in [0, 4, 5]:  # Clases de interés (Clamp)
                                # cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4)
                                # cv2.putText(frame, f"{class_names[class_id]}", (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                                # Recortar la región de interés
                                frame2 = frame[y1:y2, x1:x2]

                                # Guardar el recorte en el directorio de salida
                                output_file = f"{class_names[class_id]}_{img_file}"
                                output_path = os.path.join(output_dir, output_file)
                                cv2.imwrite(output_path, frame2)

            cv2.imshow("frame", frame)
            if (cv2.waitKey(1) & 0xFF == ord('q')):
                cv2.destroyAllWindows()
                break

if __name__ == "__main__":
    main()



#Tengo una carpeta con 6 carpeta que contienen imagenes, quisiera que hagas un script con python y verifiques el tamano de largo y ancho de cada imagen