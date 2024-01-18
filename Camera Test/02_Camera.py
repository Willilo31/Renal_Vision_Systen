import cv2

url1 = 'rtsp://root:admin@192.168.0.11:554/axis-media/media.amp'
url2 = 'rtsp://root:jetson@192.168.0.12:554/axis-media/media.amp'
url3 = 'rtsp://root:jetson@192.168.0.13:554/axis-media/media.amp'
url4 = 'rtsp://root:jetson@192.168.0.14:554/axis-media/media.amp'

cap1 = cv2.VideoCapture(url1)
cap2 = cv2.VideoCapture(url2)
cap3 = cv2.VideoCapture(url3)
cap4 = cv2.VideoCapture(url4)

cap1.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap1.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
cv2.namedWindow("Frame_1", cv2.WINDOW_NORMAL)

cap2.set(cv2.CAP_PROP_FRAME_WIDTH,416)
cap2.set(cv2.CAP_PROP_FRAME_HEIGHT,380)
cv2.namedWindow("Frame_2", cv2.WINDOW_NORMAL)

cap3.set(cv2.CAP_PROP_FRAME_WIDTH,416)
cap3.set(cv2.CAP_PROP_FRAME_HEIGHT,380)
cv2.namedWindow("Frame_3", cv2.WINDOW_NORMAL)

cap4.set(cv2.CAP_PROP_FRAME_WIDTH,416)
cap4.set(cv2.CAP_PROP_FRAME_HEIGHT,380)
cv2.namedWindow("Frame_4", cv2.WINDOW_NORMAL)

while True:

    success1, frame1 = cap1.read()
    success2, frame2 = cap2.read()
    success3, frame3 = cap3.read()
    success4, frame4 = cap4.read()

    cv2.imshow("Frame_1", frame1)
    cv2.imshow("Frame_2", frame2)
    cv2.imshow("Frame_3", frame3)
    cv2.imshow("Frame_4", frame4)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap1.release()
cap2.release()
cap3.release()
cap4.release()
cv2.destroyAllWindows()
