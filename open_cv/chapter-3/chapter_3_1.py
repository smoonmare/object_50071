import cv2

img = cv2.imread("../test_pic.jpg")
print(img.shape)
# image with (y, x)

imgResize = cv2.resize(img, (425, 640))
# image with (y, x)

cv2.imshow("Default image", img)
cv2.imshow("Resized image", imgResize)
cv2.waitKey(0)