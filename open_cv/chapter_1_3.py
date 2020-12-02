#!/usr/local/bin/python3.7

import cv2

cap = cv2.VideoCapture(0)
# "0" stands for default aka webcam.

cap.set(3, 640)
cap.set(4, 480)

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)

    # Waits for keyboard input "q" to stop a script
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break