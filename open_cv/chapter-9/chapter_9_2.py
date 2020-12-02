import cv2

cap = cv2.VideoCapture(0)
# "0" stands for default aka webcam.

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap.set(3, 640)
cap.set(4, 480)

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (57, 255, 20), 2)

    cv2.imshow("Face Recognition from live feed", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break