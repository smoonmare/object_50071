import cv2
import numpy as np

img = cv2.imread("../cards.jpg")

width, height = 250, 350
point1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])
# 4 pairs of corresponding points on and image
# x1,y1 | x2,y2 top line of the card
point2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
# 4 pairs of corresponding points for destination perspective
# x1,y1 | x2,y2 top line of the card
matrix = cv2.getPerspectiveTransform(point1, point2)
# Creates matrix from 4 corresponding points
imgOut = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Stock image", img)
cv2.imshow("Warped image", imgOut)
cv2.waitKey(0)