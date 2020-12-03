import cv2
import numpy as np


def preProcessing(img, kernel):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv2.Canny(imgBlur, 200, 200)
    imgDila = cv2.dilate(imgCanny, kernel, iterations=2)
    imgThresh = cv2.erode(imgDila, kernel, iterations=1)

    return imgThresh


def getContour(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    max_area = 0
    ideal = np.array([])

    for contour in contours:
        area = cv2.contourArea(contour)

        if area > 5000:
            cv2.drawContours(imgContour, contour, -1, (255, 0, 0), 20)
            perimeter = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
            # Corner points of the contour  figures
            if area > max_area & len(approx) == 4:
                ideal = approx
                max_area = area
        return ideal


img_width = 640
img_height = 480
capture = cv2.VideoCapture(0)
capture.set(3, img_width)
capture.set(4, img_height)
capture.set(11, 15)
capture.set(10, -50)

kernel = np.ones((5, 5))

while True:
    success, img = capture.read()
    img = cv2.resize(img, (img_width, img_height))
    imgContour = img.copy()
    imgThresh = preProcessing(img, kernel)
    getContour(imgThresh)
    cv2.imshow("Live Feed Output", img)
    cv2.imshow("Image Threshold", imgThresh)
    cv2.imshow("Contour Box", imgContour)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break