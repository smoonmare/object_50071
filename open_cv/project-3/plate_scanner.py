import cv2


plate_number_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_russian_plate_number.xml")


def find_plate(img_in):
    # x, y, w, h = 0, 0, 0, 0
    plates = plate_number_cascade.detectMultiScale(img_in, 1.3, 4)
    for (x, y, w, h) in plates:
        img_out = cv2.rectangle(img_in, (x, y), (x + w, y + h), (57, 255, 20), 2)
        plate_img = img_in[y:y+h, x:x+w]
    return img_out, plate_img


img = cv2.imread("car.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img, plate = find_plate(img)
cv2.imshow("Input Feed", img)
cv2.imwrite("plate.jpg.jpg", plate)
cv2.waitKey(0)