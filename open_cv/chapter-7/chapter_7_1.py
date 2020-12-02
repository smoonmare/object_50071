import cv2
import numpy as np

# Image load
path = "../test_pic.jpg"
img = cv2.imread(path)
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Trackbar window
cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar", 640, 240)
cv2.createTrackbar("Hue min", "Trackbar", 39, 179, lambda x:x)  # lambda for self call
cv2.createTrackbar("Hue max", "Trackbar", 179, 179, lambda x:x)
cv2.createTrackbar("Sat min", "Trackbar", 0, 255, lambda x:x)
cv2.createTrackbar("Sat max", "Trackbar", 255, 255, lambda x:x)
cv2.createTrackbar("Val min", "Trackbar", 0, 255, lambda x:x)
cv2.createTrackbar("Val max", "Trackbar", 255, 255, lambda x:x)

while True:
    # Transformation to HSV
    h_min = cv2.getTrackbarPos("Hue min", "Trackbar")
    h_max = cv2.getTrackbarPos("Hue max", "Trackbar")
    s_min = cv2.getTrackbarPos("Sat min", "Trackbar")
    s_max = cv2.getTrackbarPos("Sat max", "Trackbar")
    v_min = cv2.getTrackbarPos("Val min", "Trackbar")
    v_max = cv2.getTrackbarPos("Val max", "Trackbar")
    # Mask creation for the color range
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    # new image copies from masked pixels
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    # Image show
    # cv2.imshow("Stock image", img)
    # cv2.imshow("HSV image", imgHSV)
    cv2.imshow("Mask", mask)
    cv2.imshow("New Image", imgResult)
    cv2.waitKey(1)