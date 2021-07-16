"""
Refer Mediapipe Documentation for Selfie Segmentation:
https://google.github.io/mediapipe/solutions/selfie_segmentation.html
"""
import cv2
import mediapipe as mp
import numpy as np

mp_draw = mp.solutions.drawing_utils

mp_selfie_segmentation = mp.solutions.selfie_segmentation

selfie_segmentation_model = mp_selfie_segmentation.SelfieSegmentation()

bg_img = cv2.imread("Images/space_background.jpg")

cap = cv2.VideoCapture(0)

while cap.isOpened():
    flag, frame = cap.read()
    if not flag:
        print("Camera not Accessible")

    results = selfie_segmentation_model.process(frame)
    """Condition is putted here, becoz if we will run the cv2.imshow with results.segmentation_mask
    we will see that there is alot of noise with the mask of my body. To nulify that we are using
    this condition"""
    condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1
    if bg_img is None:
        bg_img = np.zeros(frame.shape, dtype=np.uint8)
        bg_img[:] = (0, 255, 0)
    else:
        bg_img = cv2.resize(bg_img, (frame.shape[1], frame.shape[0]))
    output_img = np.where(condition, frame, bg_img)
    # cv2.imshow("Segmentation Raw", results.segmentation_mask)
    cv2.imshow("Final Frame", output_img)
    # cv2.imshow("Original Frame", frame)
    if cv2.waitKey(10) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
