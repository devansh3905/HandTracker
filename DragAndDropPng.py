import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

detector = HandDetector(detectionCon=0.65)

img1 = cv2.imread("operator2.jpg")
[ox, oy] = 50, 50

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)

    if hands:
        lmList = hands[0]['lmList']
        cursor = lmList[8]
        length, info, img = detector.findDistance(lmList[8],lmList[12], img)
        print(length)
        if length < 60:
            cursor = lmList[8]
            if ox<cursor[0]<ox+w and oy<cursor[1]<oy+h:
                ox , oy = cursor[0] -w//2, cursor[1] - h//2
    h, w, _ = img1.shape
    img[oy:oy+h, ox:ox+w] = img1

    cv2.imshow("Image", img)
    cv2.waitKey(1)