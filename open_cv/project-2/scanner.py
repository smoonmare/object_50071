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
        print(area)
        if area > 60000:
            perimeter = cv2.arcLength(contour, True)
            print(perimeter)
            approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
            print(approx)
            print(len(approx))
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
    print(points)
    points = reorder_points(points)
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
    except ValueError:
        print("No document detected")
    except AttributeError:
        print("Moving too fast")
    cv2.imshow("Live Feed Output", img)
    cv2.imshow("Image Threshold", img_thresh)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break