import cv2
import numpy as np


# Change the value below if needed.
videoFeed = cv2.VideoCapture(1)

while True:
    ret, frame = videoFeed.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    low_red = np.array([0, 100, 20])
    high_red = np.array([5, 255, 255])

    low_green = np.array([50, 100, 20])
    high_green = np.array([70, 255, 255])


    red_mask = cv2.inRange(hsv, low_red, high_red)
    green_mask = cv2.inRange(hsv, low_green, high_green)

    rg_mask = red_mask + green_mask

    red_green_filter_camera = cv2.bitwise_and(frame, frame, mask=rg_mask)

    cv2.imshow('Result', red_green_filter_camera)

    if cv2.waitKey(1) == ord('q'):
        break


videoFeed.release()
cv2.destroyAllWindows()