import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

cv2.rectangle(img, (0, 0), (300, 400), (0, 0, 100), 3)
# rectangle with x1,y1 = 0,0 | x2,y2 = 300, 400

cv2.circle(img, (256, 256), 40, (0, 135, 0), 2)
# circle with x,y = 256, 256 | r = 40

cv2.putText(img, "Test", (306, 356), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (133, 122, 144), 1)
# text with start in x,y = 306, 356 | custom font | scale = 2

cv2.imshow("Figures on a dark", img)
cv2.waitKey(0)
