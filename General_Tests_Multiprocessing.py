import cv2
from ultralytics import YOLO
import time
from multiprocessing import Process

def process_video(process_id, model_path):
    model = YOLO(model_path)

    cap = cv2.VideoCapture(process_id)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    prev_frame_time = time.time()
    new_frame_time = 0

    while cap.isOpened():
        success, frame = cap.read()

        if success:
            new_frame_time = time.time()

            results = model(frame, device=0, imgsz=640, conf=0.50, agnostic_nms=True)
            annotated_frame = results[0].plot()

            fps = 1 / (new_frame_time - prev_frame_time)
            prev_frame_time = new_frame_time

            fps_text = f"FPS: {fps:.2f}"

            cv2.putText(annotated_frame, fps_text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            cv2.imshow(f"Frame_{process_id}", annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    url1 = 'rtsp://root:admin@192.168.0.11:554/axis-media/media.amp'
    url2 = 'rtsp://root:jetson@192.168.0.12:554/axis-media/media.amp'
    url3 = 'rtsp://root:jetson@192.168.0.13:554/axis-media/media.amp'
    url4 = 'rtsp://root:jetson@192.168.0.14:554/axis-media/media.amp'
    url5 = 'rtsp://root:jetson@192.168.0.15:554/axis-media/media.amp'

    model_path1 = 'yolov8n.pt'

    process1 = Process(target=process_video, args=(url1, model_path1))
    process2 = Process(target=process_video, args=(url2, model_path1))

    process1.start()
    process2.start()

    process1.join()
    process2.join()
