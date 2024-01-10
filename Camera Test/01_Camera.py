import cv2

cap1 = cv2.VideoCapture(0)

cap1.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap1.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
cv2.namedWindow("Frame_1", cv2.WINDOW_NORMAL)

while True:

    success1, frame1 = cap1.read()

    cv2.imshow("Frame_1", frame1)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap1.release()

cv2.destroyAllWindows()
