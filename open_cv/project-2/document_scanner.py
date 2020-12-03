import cv2
import numpy as np


feed_list = []
doc_view = []
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
    img_blur = cv2.GaussianBlur(img_gray, (9, 9), 1)
    img_canny = cv2.Canny(img_blur, 200, 200)
    img_dil = cv2.dilate(img_canny, heart, iterations=2)
    img_out = cv2.erode(img_dil, heart, iterations=1)
    return img_out


def get_contour(img_in):
    """
    Function designed for detecting rectangular shaped
    objects aka documents.
    :param img_in: input from feed
    :return: corner points(unordered)
    corner_points = [a[x1,y1], b[x2,y2, c[x3.y3], d[x4,y4]]
    """
    max_area = 0
    corner_points = np.array([])
    contours, hierarchy = cv2.findContours(img_in, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv2.contourArea(contour)
        # print(area)
        if area > 60000:
            perimeter = cv2.arcLength(contour, True)
            # print(perimeter)
            approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
            # print(approx)
            # print(len(approx))
            # Corner points of the contour  figures
            if area > max_area and len(approx) == 4:
                corner_points = approx
                max_area = area
        cv2.drawContours(img_contour, corner_points, -1, (255, 0, 0), 20)
        return corner_points


def reorder_points(points_in):
    """
    Function for reordering the corner points
    of found document to match the pattern of
    point_2 in get_warp() function.
    :param points_in: corner points of the found document
    :return: reordered corner points
    """
    points_in = points_in.reshape((4, 2))
    points_out = np.zeros((4, 1, 2), np.int32)
    points_sum = points_in.sum(1)
    points_diff = np.diff(points_in, axis=1)
    # print(points_in)
    # print(points_sum)
    # print(points_diff)
    points_out[0] = points_in[np.argmin(points_sum)]
    points_out[3] = points_in[np.argmax(points_sum)]
    points_out[1] = points_in[np.argmin(points_diff)]
    points_out[2] = points_in[np.argmax(points_diff)]
    return points_out


def get_warp(img_in, points):
    """
    Warping based on top and bottom points
    of the scanned document
    :param img_in: input feed
    :param points: corner points of the document
    :return: warped image
    """
    # print(points)
    points = reorder_points(points)
    point_1 = np.array(points, np.float32)
    point_2 = np.array([[0, 0], [img_width, 0], [0, img_height], [img_width, img_height]], np.float32)
    matrix = cv2.getPerspectiveTransform(point_1, point_2)
    img_out = cv2.warpPerspective(img_in, matrix, (img_width, img_height))
    img_out = img_out[20:img_out.shape[0]-20, 20:img_out.shape[1]-20]
    img_out = cv2.resize(img_out, (img_width, img_height))
    return img_out


def stack_images(scale, img_array):
    """
    Function for stacking images.
    :param scale: scaling multiplier
    :param img_array: an array of images for stack
    img_array = (row[item1, item2],
                 row[item3, item4],
                 row[item5, item6])
    :return: stack of images
    Source: https://github.com/murtazahassan/Learn-OpenCV-in-3-hours/blob/master/chapter6.py
    """
    rows = len(img_array)
    columns = len(img_array[0])
    rows_available = isinstance(img_array[0], list)
    width = img_array[0][0].shape[1]
    height = img_array[0][0].shape[0]
    if rows_available:
        for x in range(0, rows):
            for y in range(0, columns):
                if img_array[x][y].shape[:2] == img_array[0][0].shape[:2]:
                    img_array[x][y] = cv2.resize(img_array[x][y],
                                                 (0, 0),
                                                 None, scale, scale)
                else:
                    img_array[x][y] = cv2.resize(img_array[x][y],
                                                 (img_array[0][0].shape[1], img_array[0][0].shape[0]),
                                                 None, scale, scale)
                if len(img_array[x][y].shape) == 2:
                    img_array[x][y] = cv2.cvtColor(img_array[x][y], cv2.COLOR_GRAY2BGR)
        img_blank = np.zeros((height, width, 3), np.uint8)
        horizontal = [img_blank] * rows
        for x in range(0, rows):
            horizontal[x] = np.hstack(img_array[x])
        vertical = np.vstack(horizontal)
    else:
        for x in range(0, rows):
            if img_array[x].shape[:2] == img_array[0].shape[:2]:
                img_array[x] = cv2.resize(img_array[x], (0, 0), None, scale, scale)
            else:
                img_array[x] = cv2.resize(img_array[x],
                                          (img_array[0].shape[1], img_array[0].shape[0]),
                                          None, scale, scale)
            if len(img_array[x].shape) == 2:
                img_array[x] = cv2.cvtColor(img_array[x], cv2.COLOR_GRAY2BGR)
        horizontal = np.hstack(img_array)
        vertical = horizontal
    return vertical


while True:
    success, img = capture.read()
    img = cv2.resize(img, (img_width, img_height))
    img_contour = img.copy()
    img_thresh = pre_processing(img, kernel)
    contour_points = get_contour(img_thresh)
    try:
        img_warp = get_warp(img, contour_points)
        doc_view = ([img_warp], [img_contour])
        stack_doc_view = stack_images(0.7, doc_view)
        cv2.imshow("Found Document", stack_doc_view)
    except ValueError:
        print("No document detected")
    except AttributeError:
        print("Reshaping is broken if no lines detected")
    feed_list = ([img], [img_thresh])
    stack_feed_list = stack_images(0.7, feed_list)
    cv2.imshow("Feed / Threshold", stack_feed_list)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break