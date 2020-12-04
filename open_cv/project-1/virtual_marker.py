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


def get_contour(img_in):
    """
    Function to get center contour point
    :param img_in: input image
    :return: center of contour point
    """
    x, y, w, h = 0, 0, 0, 0
    contours, hierarchy = cv2.findContours(img_in, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500:
            perimeter = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
            x, y, w, h = cv2.boundingRect(approx)
            # cv2.draw_contours(img_result, contour, -1, (255, 0, 0), 2)
    return x + w // 2, y


def find_color(img_in, hsv, brg):
    """
    Function to detect specific color
    :param img_in: input image
    :param hsv: HSV color array
    :param brg: BRG color array
    :return: an array of points
    """
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    color_number = 0
    points_out = []

    for hsv in colors_hsv:
        lower_hsv = np.array(hsv[0:3])
        upper_hsv = np.array(hsv[3:6])
        mask = cv2.inRange(img_hsv, lower_hsv, upper_hsv)
        x, y = get_contour(mask)
        cv2.circle(img_in, (x, y), 20, brg[color_number], cv2.FILLED)
        if x != 0 and y != 0:
            points_out.append([x, y, color_number])
        color_number += 1
        # cv2.imshow(str(color[0]), mask)
    return points_out


def draw_on_canvas(canvas, points_in, colors_brg_in):
    """
    Drawing on input canvas with detected points
    :param canvas: input canvas
    :param points_in: on sharpie
    :param colors_brg_in: colors of  sharpies
    :return: nothing
    """
    for point in points_in:
        cv2.circle(canvas, (point[0], point[1]), 20, colors_brg_in[point[2]], cv2.FILLED)


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


capture = cv2.VideoCapture(0)
capture.set(3, frame_width)
capture.set(4, frame_height)
capture.set(11, 45)
capture.set(10, 25)

while True:
    success, img = capture.read()
    img_canvas = img.copy()
    key = cv2.waitKey(1)
    if key == ord("q"):
        cv2.destroyAllWindows()
        break
    else:
        new_points = find_color(img, colors_hsv, colors_bgr)
        if len(new_points) != 0:
            for new_point in new_points:
                points.append(new_point)
        if len(points) != 0:
            draw_on_canvas(img_canvas, points, colors_bgr)
        stack_feed_list = ([img_canvas, img])
        stack_feed = stack_images(0.9, stack_feed_list)
        cv2.imshow("Live Feed / Drawing", stack_feed)
        # cv2.imshow("Live Feed Output", img)
        # cv2.imshow("Contour Box", img_result)