import os
import cv2
from ultralytics import YOLO

def main():
    model = YOLO("Renal_Model_S5.pt")
    class_names = ["Blue_Clamp", "Pull_Ring_T", "Pull_Ring_II", "Pull_Ring_III", "Red_Clamp", "White_Clamp", "White_Paper_Band"]

    output_dir = "Frame_reducidos"
    rotated_output_dir = "Frame_reducidos_rotated"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    if not os.path.exists(rotated_output_dir):
        os.makedirs(rotated_output_dir)

    img_folder = "IMGS"
    total_width = 0
    total_height = 0
    total_images = 0

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
                                frame2 = frame[y1:y2, x1:x2]
                                total_images += 1
                                total_height += frame2.shape[0]
                                total_width += frame2.shape[1]

                                if total_images % 2 == 0:
                                    frame2_rotated = cv2.rotate(frame2, cv2.ROTATE_180)
                                    output_path_rotated = os.path.join(rotated_output_dir, f"{class_names[class_id]}_{img_file[:-4]}_rotated.jpg")
                                    cv2.imwrite(output_path_rotated, frame2_rotated)
                                else:
                                    output_file = f"{class_names[class_id]}_{img_file}"
                                    output_path = os.path.join(output_dir, output_file)
                                    cv2.imwrite(output_path, frame2)   
                                
            cv2.imshow("frame", frame)
            if (cv2.waitKey(1) & 0xFF == ord('q')):
                cv2.destroyAllWindows()
                break

    if total_images > 0:
        average_width = total_width / total_images
        average_height = total_height / total_images
        print(f"Ancho promedio: {average_width} pixeles")
        print(f"Largo promedio: {average_height} pixeles")

if __name__ == "__main__":
    main()
