import math
import cv2
cap = cv2.VideoCapture('Videos/vid (1).mp4')
while True:
    #sucess, img = cap.read()
    img = cv2.imread("assets/images/Ball.png")
    img = cv2.resize(img, (0, 0), None, 0.7, 0.7)
    cv2.imshow("Image", img)
    cv2.waitKey(50)


