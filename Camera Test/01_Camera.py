import cv2
import time 

url = 'rtsp://root:admin@192.168.0.11:554/axis-media/media.amp'

cap1 = cv2.VideoCapture(url)

cap1.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap1.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
cv2.namedWindow("Frame_1", cv2.WINDOW_NORMAL)

while True:

    success1, frame1 = cap1.read()

    cv2.imshow("Frame_1", frame1)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
    time.sleep(0.5)

cap1.release()

cv2.destroyAllWindows()
