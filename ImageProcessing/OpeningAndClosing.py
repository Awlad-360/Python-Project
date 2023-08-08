import cv2
import numpy as np
from google.colab.patches import cv2_imshow
img = cv2.imread('mango.jpg', 0)
kernel = np.ones((5, 5), np.uint8)
img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=1)
opening=img_erosion+img_dilation
closing=img_dilation-img_erosion
cv2_imshow(img)
cv2_imshow(opening)
cv2_imshow(closing)
cv2.waitKey(0)
