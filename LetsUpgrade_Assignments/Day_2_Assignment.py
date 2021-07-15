"""In this One, will see how to load a video & do some fun activities on that"""
import cv2
import numpy as np

# capture = cv2.VideoCapture("Videos/video.mp4")  # For running a Video stored in Local System
capture = cv2.VideoCapture(0)  # For running the Web Cam

while capture.isOpened():
    sucess, frame = capture.read()
    if sucess:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gray Frame", gray_frame)
        # cv2.imshow("Frame", frame)
        zeros = np.zeros((frame.shape[0], frame.shape[1]), np.uint8)
        r, g, b = cv2.split(frame)

        red = cv2.merge([r, zeros, zeros])
        green = cv2.merge([zeros, g, zeros])
        blue = cv2.merge([zeros, zeros, b])

        cv2.imshow("Red", red)
        cv2.imshow("Green", green)
        cv2.imshow("Blue", blue)

        amplified_frame = cv2.merge([r + 100, g + 95, b + 78])
        cv2.imshow("Amplified Image", amplified_frame)

        cv2.rectangle(frame, (200, 200), (400, 400), (200, 200, 200), 5)
        cv2.putText(frame, "Assignment For Day-2 Completed", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow("Frame", frame)

        k = cv2.waitKey(50)  # For Slow Motioning Video {50 Milli-Seconds}
        """Note: For making each frame run 5 seconds slower, put 5000"""
        if k == ord('q'):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()
