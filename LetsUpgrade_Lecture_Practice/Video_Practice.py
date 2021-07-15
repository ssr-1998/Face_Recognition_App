"""In this One, will see how to load a video & do some fun activities on that"""
import cv2
import numpy as np

# capture = cv2.VideoCapture("Videos/video.mp4")  # For running a Video stored in Local System
capture = cv2.VideoCapture(0)  # For running the Web Cam
"""Note: Video is loading in BGR"""

while capture.isOpened():
    sucess, frame = capture.read()
    if sucess:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        cv2.imshow("Gray Frame", gray_frame)
        cv2.imshow("Frame", frame)

        k = cv2.waitKey(50)  # For Slow Motioning Video {50 Milli-Seconds}
        """Note: For making each frame run 5 seconds slower, put 5000"""
        if k == ord('q'):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()
