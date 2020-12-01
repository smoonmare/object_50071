#!/usr/local/bin/python3.7
import cv2

print("mission success")

img = cv2.imread("test_pic.jpg")

cv2.imshow("Output", img)
cv2.waitKey(0)
