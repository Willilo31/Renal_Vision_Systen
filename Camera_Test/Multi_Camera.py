import cv2
from multiprocessing import Process

def process_video(ID, process_id):

    cap = cv2.VideoCapture(process_id)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while cap.isOpened():
        success, frame = cap.read()

        if success:
            cv2.imshow(f"Frame_{ID}", frame)

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

    process1 = Process(target=process_video, args=(11, url1,))
    process2 = Process(target=process_video, args=(12, url2,))
    process3 = Process(target=process_video, args=("USB", 0,))
    process4 = Process(target=process_video, args=("USB2", 4,))
    # process5 = Process(target=process_video, args=(15, url5,))

    process1.start()
    process2.start()
    process3.start()
    process4.start()
    # process5.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()
    # process5.join()