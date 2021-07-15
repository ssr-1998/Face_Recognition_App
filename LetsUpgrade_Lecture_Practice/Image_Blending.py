import cv2

"""Blending Image on Another Image"""

# img1 = cv2.imread("../Images/space_background.jpg")
# img2 = cv2.imread("../Images/free.jpg")
#
"""Resizing the Background, as its shape is bigger."""
# img1_new = cv2.resize(img1, (img2.shape[1], img2.shape[0]))
#
# print(img1.shape)
# print(img1_new.shape)
# print(img2.shape)
#
"""Not Very Useful Technique, as nothing is clear in image."""
# img = img1_new + img2
#
"""Let's now try Blending
In addWeighted Function:
1. Image 1
2. Alpha (How much Image 1 will contribute to make the Final Image)
3. Image 2
4. Beta (How much Image 2 will contribute to make the Final Image)
5. Gamma
"""
# blended_img = cv2.addWeighted(img1_new, 0.6, img2, 0.4, gamma=0.0)
#
# cv2.imshow("Old Technique Blending", img)
# cv2.imshow("New Technique Blending", blended_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

"""Blending Image on WebCam"""

cap = cv2.VideoCapture(0)
img = cv2.imread("Images/space_background.jpg")

while True:
    flag, frame = cap.read()
    if not flag:
        print("Could not access the WebCam")
        break
    else:
        img = cv2.resize(img, (frame.shape[1], frame.shape[0]), )
        blended_frame = cv2.addWeighted(frame, 0.6, img, 0.4, gamma=0.1)
        x = cv2.imshow("Blended Frame", blended_frame)
        if cv2.waitKey(10) == ord("q"):
            break
cap.release()
cv2.destroyAllWindows()
