import cv2

img = cv2.imread("test_pic.jpg")

imgCropped = img[100:200, 200:500]
# Cropped chunk from (y1, y2 = 100, 200; x1, x2 = 200, 500)

cv2.imshow("Default image", img)
cv2.imshow("Cropped part", imgCropped)
cv2.waitKey(0)