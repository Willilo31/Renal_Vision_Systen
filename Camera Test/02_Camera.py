import cv2

cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(4)

cap1.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap1.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
cv2.namedWindow("Frame_1", cv2.WINDOW_NORMAL)

cap2.set(cv2.CAP_PROP_FRAME_WIDTH,416)
cap2.set(cv2.CAP_PROP_FRAME_HEIGHT,380)
cv2.namedWindow("Frame_2", cv2.WINDOW_NORMAL)

while True:

    success1, frame1 = cap1.read()
    success2, frame2 = cap2.read()

    cv2.imshow("Frame_1", frame1)
    cv2.imshow("Frame_2", frame2)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()
