"""Let's learn how to Draw anything on a Blank Canvas"""

import numpy as np
import cv2

canvas = np.zeros((512, 512, 3), np.uint8)
cv2.imshow("Blank Canvas", canvas)

cv2.line(canvas, (0, 512), (512, 0), (0, 255, 0), 2)
cv2.line(canvas, (100, 512), (512, 0), (0, 255, 0), 2)
cv2.line(canvas, (0, 400), (512, 0), (0, 255, 0), 2)

cv2.line(canvas, (0, 512), (512, 100), (0, 255, 0), 2)
cv2.line(canvas, (0, 512), (400, 0), (0, 255, 0), 2)
cv2.imshow("After Putting Lines on Canvas", canvas)

cv2.rectangle(canvas, (0, 0), (400, 400), (255, 0, 0), 5)
cv2.putText(canvas, "S.S.R", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)
cv2.imshow("Final Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
