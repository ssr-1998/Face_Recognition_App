"""
Notes:
    An affine transformation is any transformation that preserves collinearity (i.e., all points lying on
    a line initially still lie on a line after transformation) and ratios of distances (e.g., the midpoint
    of a line segment remains the midpoint after transformation).
"""

import cv2
import numpy as np

img = cv2.imread("Images/dog.jpg")
height, width = img.shape[:2]

"""
Shifting Image from one coordinates to some other.

In Translation Matrix, these [1, 0, 50] & [0, 1, 50] actually mean that we are telling the system to
Shift the Image from (1,0) coordinate to (0, 1) by 50 pixels.
"""
translation_M = np.float32([[1, 0, 50], [0, 1, 50]])  # Matrix
translated_img = cv2.warpAffine(img, translation_M, (height, width))

"""
Rotating Images

90 is the angle & 1 is the scale.
1 means to rotate same image towards left.
-1 means to rotate same image towards right
If we will increase the value of scale, the rotation will happen but with zooming in the image.
"""
rotation_M = cv2.getRotationMatrix2D((height/2, width/2), 90, 2)
rotated_img = cv2.warpAffine(img, rotation_M, (height, width))

"""
Scaling means to stretch the image.
fx & fy accepts only non-negative numbers(can be integers or float).
Here, I doubled the height of Image by giving fy=2 but as fx=1. So, the widht will remain same
"""
scaling_img = cv2.resize(img, None, fx=1, fy=2)

cv2.imshow("image", img)
cv2.imshow("translated image", translated_img)
cv2.imshow("rotated image", rotated_img)
cv2.imshow("scaled image", scaling_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
