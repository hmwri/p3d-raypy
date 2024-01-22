import numpy as np
from PIL import Image

img = Image.open("meadow_2_2k.jpg")

array = np.array(img)

import cv2


img = cv2.cvtColor(array, cv2.COLOR_RGBA2BGR)
img = cv2.imread("meadow_2_2k.png")

cv2.imshow("a",img)
cv2.imwrite("a.jpg",img)
cv2.waitKey()