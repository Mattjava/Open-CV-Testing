import cv2
import numpy as np

# Change value below to whatever value your camera is on your device.
videoFeed = cv2.VideoCapture(0)

while True:
    ret, frame = videoFeed.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    low_red = np.array([0, 200, 20])
    high_red = np.array([5, 255, 255])

    red_mask = cv2.inRange(hsv, low_red, high_red)
    red_filter_camera = cv2.bitwise_and(frame, frame, mask=red_mask)

    cv2.imshow('Result', red_filter_camera)

    if cv2.waitKey(1) == ord('q'):
        break


videoFeed.release()
cv2.destroyAllWindows()
