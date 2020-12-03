import cv2
import numpy as np

kernel = np.ones((5, 5))
img_width = 640
img_height = 480
capture = cv2.VideoCapture(0)
capture.set(3, img_width)
capture.set(4, img_height)
capture.set(11, 15)
capture.set(10, -50)


def pre_processing(img_in, heart):
    img_gray = cv2.cvtColor(img_in, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (5, 5), 1)
    img_canny = cv2.Canny(img_blur, 200, 200)
    img_dil = cv2.dilate(img_canny, heart, iterations=2)
    img_out = cv2.erode(img_dil, heart, iterations=1)
    return img_out


def get_contour(img_in):
    contours, hierarchy = cv2.findContours(img_in, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    max_area = 0
    corner_points = np.array([])

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 5000:
            perimeter = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
            # Corner points of the contour  figures
            if area > max_area & len(approx) == 4:
                corner_points = approx
                max_area = area
        cv2.drawContours(img_contour, contour, -1, (255, 0, 0), 20)
        return corner_points


def get_warp(img_in, points):
    point_1 = np.array(points, np.float32)
    point_2 = np.array([[0, 0], [img_width, 0], [0, img_height], [img_width, img_height]], np.float32)
    matrix = cv2.getPerspectiveTransform(point_1, point_2)
    img_out = cv2.warpPerspective(img_in, matrix, (img_width, img_height))

    return img_out


while True:
    success, img = capture.read()
    img = cv2.resize(img, (img_width, img_height))
    img_contour = img.copy()
    img_thresh = pre_processing(img, kernel)
    try:
        contour_points = get_contour(img_thresh)
        img_warp = get_warp(img, contour_points)
        cv2.imshow("Contour Box", img_contour)
        cv2.imshow("Warped Image", img_warp)
    except:
        print("No document detected")
    # cv2.imshow("Live Feed Output", img)
    cv2.imshow("Image Threshold", img_thresh)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.destroyAllWindows()