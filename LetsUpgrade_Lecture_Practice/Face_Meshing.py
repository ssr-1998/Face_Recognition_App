"""
Refer Mediapipe Documentation for Face Meshing:
https://google.github.io/mediapipe/solutions/face_mesh.html
"""
import cv2
import mediapipe as mp

mp_draw = mp.solutions.drawing_utils

drawing_specs = mp_draw.DrawingSpec((255, 0, 0), 1, 1)

mp_face_mesh = mp.solutions.face_mesh

face_mesh_model = mp_face_mesh.FaceMesh()

cap = cv2.VideoCapture(0)

while cap.isOpened():
    flag, frame = cap.read()
    if not flag:
        print("Camera not Accessible")
    results = face_mesh_model.process(frame)
    if results.multi_face_landmarks:
        for landmark in results.multi_face_landmarks:
            mp_draw.draw_landmarks(
                image=frame,
                landmark_list=landmark,
                connections=mp_face_mesh.FACE_CONNECTIONS,
                landmark_drawing_spec=drawing_specs,
                connection_drawing_spec=drawing_specs
            )
    cv2.imshow("Meshing", frame)
    if cv2.waitKey(10) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
