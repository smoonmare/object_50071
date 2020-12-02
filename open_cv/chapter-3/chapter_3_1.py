import cv2

img = cv2.imread("../test_pic.jpg")
print(img.shape)
# image with (x, y)

imgResize = cv2.resize(img, (425, 640))
# image with (x, y)

cv2.imshow("Default image", img)
cv2.imshow("Resized image", imgResize)
cv2.waitKey(0)