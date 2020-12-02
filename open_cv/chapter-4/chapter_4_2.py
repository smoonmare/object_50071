import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

# cv2.line(img, (0, 0), (300, 300), (0, 255, 0), 3)
# line with y1,x1 = 0,0 y2,x2 = 300,300 RGB(0,255,0) and thickness=3
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
# diagonal line

cv2.imshow("Zeros+Line", img)
cv2.waitKey(0)