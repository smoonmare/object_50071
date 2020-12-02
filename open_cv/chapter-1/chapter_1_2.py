#!/usr/local/bin/python3.7
import cv2

cap = cv2.VideoCapture("../test_video.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Waits for keyboard input "q"
        break