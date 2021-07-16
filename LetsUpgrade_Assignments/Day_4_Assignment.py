"""
Refer Mediapipe Documentation for Hand Pose Detection:
https://google.github.io/mediapipe/solutions/hands
"""
import cv2
import mediapipe as mp

mp_draw = mp.solutions.drawing_utils

mp_hand_pose = mp.solutions.hands

hand_pose_model = mp_hand_pose.Hands()

cap = cv2.VideoCapture(0)

while cap.isOpened():
    flag, frame = cap.read()
    if not flag:
        print("Camera not Accessible")

    results = hand_pose_model.process(frame)
    if results.multi_hand_landmarks:
        for landmark in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(
                image=frame,
                landmark_list=landmark,
                connections=mp_hand_pose.HAND_CONNECTIONS
            )
    cv2.imshow("Frame", frame)
    if cv2.waitKey(10) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
