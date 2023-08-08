import cv2
import numpy as np
from google.colab.patches import cv2_imshow
img = cv2.imread('/content/ainstein.jpg')
max_val = np.max(img)
c = 255 / np.log(1 + max_val)
log_Image = c * np.log(1 + img)
log_Image = np.uint8(log_Image)
print('Input Image:')
cv2_imshow(img)
print('Output Image:')
cv2_imshow(log_Image)
cv2.waitKey(0)
cv2.destroyAllWindows()
