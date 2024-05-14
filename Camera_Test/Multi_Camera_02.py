import cv2
from multiprocessing import Process
import time 

def process_video(ID, process_id):

    cap = cv2.VideoCapture(process_id)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while cap.isOpened():
        success, frame = cap.read()

        if success:
            time.sleep(0.05)
            cv2.imshow(f"Frame_{ID}", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":

    url1 = 'http://root:admin@192.168.0.11/axis-cgi/mjpg/video.cgi'
    url2 = 'http://root:jetson@192.168.0.12/axis-cgi/mjpg/video.cgi'

    process1 = Process(target=process_video, args=(11, url1,))
    process2 = Process(target=process_video, args=(12, url2,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()