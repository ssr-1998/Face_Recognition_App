"""
To see the practical example of this Convolution.
Visit: https://setosa.io/ev/image-kernels/
"""

import cv2
import numpy as np

"""Convolution on Images"""

# img = cv2.imread("Images/mc-laren.jpg")
#
# kernel = np.float32([[0, 0, 0],
#                      [0, 1, 1],
#                      [1, 1, -5]])
#
# con_img = cv2.filter2D(img, -1, kernel=kernel)
#
# cv2.imshow("con Image", con_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
