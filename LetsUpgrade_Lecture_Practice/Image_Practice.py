"""Some Fun things I learnt to do on Images"""

import cv2
import numpy as np

"""Reading Images"""
img = cv2.imread("Images/mc-laren.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# print("The Height of Image is", img.shape[0], ", width is", img.shape[1], "& the channels/layers are", img.shape[2])

"""An Array with zeros"""
zeros = np.zeros((img.shape[0], img.shape[1]), np.uint8)

"""Splitting Channels"""
r, g, b = cv2.split(img)

red = cv2.merge([r, zeros, zeros])
green = cv2.merge([zeros, g, zeros])
blue = cv2.merge([zeros, zeros, b])

cv2.imshow("Original", img)
cv2.imshow("Gray", gray_img)
cv2.imshow("Red", red)
cv2.imshow("Green", green)
cv2.imshow("Blue", blue)
cv2.waitKey(0)  # Press 0 to Destroy all Windows
cv2.destroyAllWindows()

"""Merging Image from Splitted Channels"""
# custom_img = cv2.merge([r, g, b])
# cv2.imshow("Custom", custom_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

"""Amplifying Images (Increasing the amount of colors in image)"""
# amplified_img = cv2.merge([r+100, g+95, b+78])
# cv2.imshow("Amplified Image", amplified_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
