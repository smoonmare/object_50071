'''
Viola & Jones method.
First Real-time Detection Method(2001)
OpenCV Cascades used
'''
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

img = cv2.imread("../face.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x + w, y + h), (57, 255, 20), 2)

cv2.imshow("Stock", img)
cv2.waitKey(0)