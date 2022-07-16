# import cv2
# import time
#
#
# cap = cv2.VideoCapture(0)
#
# while True:
#     imgnee = cap.read()
#     # imgnee = cv2.imread("1.jpg")
#     cv2.imshow("Image", imgnee)
#     cv2.waitKey(0)
#     print("Hello")


import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
detector = mp.solutions.hands.Hands()

while True:
    success, img = cap.read()

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result =  detector.process(img)

    if result.multi_hand_
    cv2.imshow("AI", img)
    cv2.waitKey(1)

