import cv2
import numpy as np

# Variables
frame_width = 640
frame_height = 480
# colors red, green, blue, yellow found with color_picker.py
# color = [hue_min, sat_min, val_min, hue_max, sat_max, val_max]
colors_hsv = [[148, 195, 60, 179, 255, 255],
          [31, 71, 0, 76, 255, 255],
          [89, 138, 51, 102, 255, 255],
          [17, 60, 39, 26, 255, 255]]
colors_bgr = [[0, 0, 128],
              [0, 128, 0],
              [128, 0, 0],
              [0, 128, 128]]
points = []
# [x, y, color_id]


def getContour(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0

    for contour in contours:
        area = cv2.contourArea(contour)

        if area > 500:
            perimeter = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
            x, y, w, h = cv2.boundingRect(approx)
            # cv2.drawContours(imgResult, contour, -1, (255, 0, 0), 2)
    return x + w // 2, y


def findColor(img, *args):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    color_number = 0
    new_points = []

    for color_hsv in colors_hsv:
        lower_hsv = np.array(color_hsv[0:3])
        upper_hsv = np.array(color_hsv[3:6])
        mask = cv2.inRange(imgHSV, lower_hsv, upper_hsv)
        x, y = getContour(mask)
        cv2.circle(imgResult, (x, y), 20, colors_bgr[color_number], cv2.FILLED)
        if x != 0 and y != 0:
            points.append([x, y, color_number])
        color_number += 1
        # cv2.imshow(str(color[0]), mask)
    return new_points


def drawOnCanvas(points, color_brg):
    for point in points:
        cv2.circle(imgResult, (point[0], point[1]), 20, colors_bgr[point[2]], cv2.FILLED)


capture = cv2.VideoCapture(0)
capture.set(3, frame_width)
capture.set(4, frame_height)
capture.set(11, 45)
capture.set(10, 25)
# .set() properties
# 0. CV_CAP_PROP_POS_MSEC Current position of the video file in milliseconds.
# 1. CV_CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next.
# 2. CV_CAP_PROP_POS_AVI_RATIO Relative position of the video file
# 3. CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
# 4. CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
# 5. CV_CAP_PROP_FPS Frame rate.
# 6. CV_CAP_PROP_FOURCC 4-character code of codec.
# 7. CV_CAP_PROP_FRAME_COUNT Number of frames in the video file.
# 8. CV_CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
# 9. CV_CAP_PROP_MODE Backend-specific value indicating the current capture mode.
# 10. CV_CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
# 11. CV_CAP_PROP_CONTRAST Contrast of the image (only for cameras).
# 12. CV_CAP_PROP_SATURATION Saturation of the image (only for cameras).
# 13. CV_CAP_PROP_HUE Hue of the image (only for cameras).
# 14. CV_CAP_PROP_GAIN Gain of the image (only for cameras).
# 15. CV_CAP_PROP_EXPOSURE Exposure (only for cameras).
# 16. CV_CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
# 17. CV_CAP_PROP_WHITE_BALANCE Currently unsupported
# 18. CV_CAP_PROP_RECTIFICATION Rectification flag for stereo cameras
#     (note: only supported by DC1394 v 2.x backend currently)

while True:
    success, img = capture.read()
    imgResult = img.copy()

    new_points = findColor(img, colors_hsv, colors_bgr)
    if len(new_points) != 0:
        for new_point in new_points:
            points.append(new_point)
    if len(points) != 0:
        drawOnCanvas(points, colors_bgr)

    cv2.imshow("Live Feed Output", img)
    cv2.imshow("Contour Box", imgResult)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break