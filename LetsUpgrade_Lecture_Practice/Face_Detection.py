"""
Refer Mediapipe Documentation for Face Detection:
https://google.github.io/mediapipe/solutions/face_detection.html
"""
import cv2
import mediapipe as mp

"""Detecting Face & Facial Landmarks using mediapipe Library"""

mp_drawing = mp.solutions.drawing_utils  # Draws detection on frames

"""face_detection is a module in mediapipe Library from where we will use all functions to detect face"""
mp_face_detection = mp.solutions.face_detection

model_detection = mp_face_detection.FaceDetection()  # Model for Detecting the Faces

cap = cv2.VideoCapture(0)

while cap.isOpened():
    flag, frame = cap.read()
    if not flag:
        print("Could not access the camera")
        break
    new_frame = frame.copy()
    results = model_detection.process(new_frame)
    if results.detections:
        for landmark in results.detections:  # Landmarks in face are (2 Eyes(Iris), 2 Ears, Nose & Mouth)
            mp_drawing.draw_detection(new_frame, landmark)  # This will automatically create a rectange & a point on each landmark
            print(results.detections)
    cv2.imshow("Frame", new_frame)
    if cv2.waitKey(10) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

"""Detecting Only Nose out of all Facial Landmarks using mediapipe Library"""

# mp_drawing = mp.solutions.drawing_utils
#
# mp_face_detection = mp.solutions.face_detection
#
# model_detection = mp_face_detection.FaceDetection()
#
# cap = cv2.VideoCapture(0)
#
# while cap.isOpened():
#     flag, frame = cap.read()
#     if not flag:
#         print("Camera not Accessible")
#
#     new_frame = frame.copy()
#     results = model_detection.process(new_frame)
#     if results.detections:
#         for landmark in results.detections:
#             mp_drawing.draw_detection(new_frame, landmark)
#             # print(landmark.location_data)
#             print(mp_face_detection.get_key_point(landmark, mp_face_detection.FaceKeyPoint.NOSE_TIP))
#     cv2.imshow("Nose Detection", new_frame)
#     if cv2.waitKey(10) == ord("q"):
#         break
# cap.release()
# cv2.destroyAllWindows()
