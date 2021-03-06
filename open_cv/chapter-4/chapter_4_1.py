import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# An array of 0's in shape "3" for RGB(0,0,0)

img[:] = 255, 0, 0
# all of x and y will be colored in
img[100:350, 200:450] = 0, 255, 0
# x1,x2, y1,y2 colored in RGB(0,255,0)

cv2.imshow("Zeros", img)
cv2.waitKey(0)