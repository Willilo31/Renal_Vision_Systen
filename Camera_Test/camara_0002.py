import cv2
import time 

url1 = 'http://root:admin@192.168.0.11/axis-cgi/mjpg/video.cgi'
url2 = 'http://root:jetson@192.168.0.12/axis-cgi/mjpg/video.cgi'

cap1 = cv2.VideoCapture(url1)
cap2 = cv2.VideoCapture(url2)

cap1.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap1.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
cv2.namedWindow("Frame_1", cv2.WINDOW_NORMAL)

cap2.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap2.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
cv2.namedWindow("Frame_2", cv2.WINDOW_NORMAL)

while True:

    success1, frame1 = cap1.read()
    success2, frame2 = cap2.read()
    time.sleep(0.05)
    time.sleep(0.05)
    cv2.imshow("Frame_1", frame1)
    cv2.imshow("Frame_2", frame2)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()
