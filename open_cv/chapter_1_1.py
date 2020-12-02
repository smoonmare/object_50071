#!/usr/local/bin/python3.7
import cv2

print("mission success")

# Read of the picture.
img = cv2.imread("test_pic.jpg")

# Show cv object  in a window
cv2.imshow("Output", img)
cv2.waitKey(0)
