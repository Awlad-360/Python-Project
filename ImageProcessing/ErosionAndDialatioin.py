import cv2
import numpy as np
from google.colab.patches import cv2_imshow
img = cv2.imread('ainstein.jpg', 0)
kernel = np.ones((5, 5), np.uint8)
img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=1)
print('Input Image')
cv2_imshow(img)
print('Erosion Image')
cv2_imshow(img_erosion)
print('Dialatin Image')
cv2_imshow(img_dilation)
cv2.waitKey(0)
