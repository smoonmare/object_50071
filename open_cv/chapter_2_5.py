#!/usr/local/bin/python3.7
import cv2
import numpy as np

img = cv2.imread("test_pic.jpg")
kernel = np.ones((2, 2), np.uint8)

imgCanny = cv2.Canny(img, 100, 200)
imgErosion = cv2.erode(imgCanny, kernel, iterations=1)

cv2.imshow("Edge detection", imgCanny)
cv2.imshow("Erosion Fix", imgErosion)
cv2.waitKey(0)