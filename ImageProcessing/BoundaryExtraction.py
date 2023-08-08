import cv2
import numpy as np
from google.colab.patches import cv2_imshow
img = cv2.imread('mango.jpg')
kernel = np.ones((5, 5), np.uint8)
img_erosion = cv2.erode(img, kernel, iterations=1)
boundary_extraction=img-(img_erosion)
cv2_imshow(img)
cv2_imshow(boundary_extraction)
cv2.waitKey(0)

