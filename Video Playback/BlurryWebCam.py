import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open the webcam.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.GaussianBlur(frame, (111, 111), 0)
    cv2.imshow('Webcam', frame)
    cv2.startWindowThread()

    # Break on keyboard input Q
    c = cv2.waitKey(33)
    if c == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
for i in range(2):
    cv2.waitKey(1)
