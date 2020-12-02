#!/usr/local/bin/python3.7
import cv2

img = cv2.imread("../test_pic.jpg")

imgBlur = cv2.GaussianBlur(img, (7, 7), 0)

cv2.imshow("Regular Image", img)
cv2.imshow("Blurred Image", imgBlur)
cv2.waitKey(0)