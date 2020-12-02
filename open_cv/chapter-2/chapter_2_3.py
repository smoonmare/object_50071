#!/usr/local/bin/python3.7
import cv2

img = cv2.imread("../test_pic.jpg")

imgCanny = cv2.Canny(img, 150, 200)

cv2.imshow("Edge detection", imgCanny)
cv2.waitKey(0)